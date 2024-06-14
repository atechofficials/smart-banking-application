# Smart Banking Services v1.0 GUI Window
# Developed By Mrinal Singh Tak
# This software/program/code is licensed under GNU GPLv3 
# (General Public License v3)
# For more details visit https://choosealicense.com/licenses/gpl-3.0/

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from bank_functions import *
from bank_rfid import read_rfid
import webbrowser
from tkinter import OptionMenu
from tkinter import messagebox
import os

# Function to validate Email Address
def validate_email(email):
  # Check if the email provider is gmail or not
  if email.endswith("@gmail.com"):
    return True
  else:
    return False

# Valid email address flag
valid_email = False

# Loop until a valid email address is entered
while not valid_email:
  # Ask user for admin email address input
  admin_email = input("Enter the Bank Admin Email Address: ")
  admin_email = admin_email.lower()
  
  # Check if entered email address is valid
  if validate_email(admin_email):
    valid_email = True
  else:
    print("Invalid Email Address. Please enter a valid gmail email address.")

# Set the admin email as an environment variable
os.environ['ADMIN_EMAIL'] = admin_email

# Call Create Table Function/Method
create_table()

# Create the main GUI window
root = Tk()
root.title("SmartBank Banking Services")
#root.positionfrom("program")

# Set window icon using Pillow library
# root.iconbitmap("smartbank_icon.ico")
window_icon_img = Image.open("images/icons/smartbank_icon.png")
window_icon_resize = window_icon_img.resize((64, 64)) # (width, height)
window_icon = ImageTk.PhotoImage(window_icon_resize)
root.iconphoto(True, window_icon)

# frame = Frame(root)
# frame.place(x=0, y=0)

image_references = []

# Server Message display duration in milliseconds
message_timeout = 3000 # 3-seconds

# def clear_frame():
#   for widget in frame.winfo_children():
#     widget.destroy()

def clear_root():
  for widget in root.winfo_children():
    widget.destroy()

# URL open Function
def link_open_func(url):
  webbrowser.open_new_tab(url)

# Function to input clear fields in forms
def clear_fields(*args):
  for field in args:
    field.delete(0, END)

def window_fix_pos(widget, window_width, window_height):
  screen_width = widget.winfo_screenwidth()
  screen_height = widget.winfo_screenheight()
  x_position = (screen_width // 2) - (window_width // 2)
  y_position = (screen_height // 2) - (window_height // 2)
  return x_position, y_position

# def get_widget_x_position(widget):
#     x_position = widget.winfo_x()
#     return x_position

# def get_widget_y_position(widget):
#     y_position = widget.winfo_y()
#     return y_position

def show_footer(window_width, window_height):

  window_width_percent = 89
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  footer_l1 = Label(root, text="Copyright © 2023-2024 Smart Banking Services. All rights reserved.", font=("Times", "12", "bold"), fg="#000000", bg="#FE9A00", width=reduced_window_width, height=1, justify="center")
  footer_l1.place(x=0, y=window_height-90)
  
  footer_l2 = Label(root, text="Developed by", font=("Times", "12"), fg="#002D62", bg="#ECC0C9", width=int(reduced_window_width/2), height=1, justify="right")
  footer_l2.place(x=0, y=window_height-60)

  footer_l3 = Label(root, text="Mrinal Singh Tak", font=("Times", "12", "bold italic"), fg="#002D62", bg="#89CFF0", width=int(reduced_window_width/2), height=1, justify="left", cursor="hand2")
  footer_l3.place(x=window_width/2, y=window_height-60)
  footer_l3.bind("<Button-1>", lambda e:
                 link_open_func("https://github.com/atechofficials"))
  
  footer_l4 = Label(root, text="Licensed under General Public License v3", font=("Times", "12"), fg="#AA0000", bg="#ECC0C9", width=reduced_window_width, height=1, cursor="hand2")
  footer_l4.place(x=0, y=window_height-30)
  footer_l4.bind("<Button-2>", lambda e:
                 link_open_func("https://choosealicense.com/licenses/gpl-3.0/"))

# Function to validate form entries
def validate_entries(entries):
  for entry in entries:
    if not entry.get():
      return False
  return True

# Function to limit entry field values
def limit_size(entry, limit):
  #def callback(input):
  def callback(P):
    #if len(entry.get()) < limit:
    if len(P) < limit:
      return True
    else:
      return False
  return callback

def show_registration_form():
  def submit_registration():
    # Check if all the entries are filled
    if not validate_entries([entry_name, entry_contact, entry_email, entry_card_number]):
      messagebox.showerror("Error", "Please fill in all the entry fields.")
      return
    
    # Entry Field Validation
    # Check if the name contains only alphabetic characters
    # if not entry_name.get().isalpha():
    #   messagebox.showerror("Error", "Invalid Name\nPlease enter alphabetic characters only.")
    #   return

    # Check if the contact number is a numeric value
    if not entry_contact.get().isdigit():
      messagebox.showerror("Error", "Invalid Contact Number\nPlease enter numeric values only.")
      return
    
    email_address = str(entry_email.get())+str(clicked.get())
    result = client_reg(entry_name.get(), entry_contact.get(), email_address, str(entry_card_number.get()))
    reg_l6 = Label(registration_window, text=result, font=("Times", "15"), width=40, height=5, justify="center", bg="#95F2FF")
    reg_l6.place(x=100, y=240)
    #messagebox.showinfo("Registration", result)
    clear_fields(entry_name, entry_contact, entry_email, entry_card_number)
    reg_l6.after(message_timeout, lambda: reg_l6.destroy())
  
  # registration_window = frame
  registration_window = root

  # Set window dimensions
  window_width = 620
  window_height = 480
  
  # Fix GUI Window Initial Position
  x, y = window_fix_pos(registration_window, window_width, window_height)

  registration_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  clear_root()

  # Set window title
  registration_window.title("Client Registration")

  x_gap = 130
  y_gap = 30

  window_width_percent = 91
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  # Heading
  reg_h1 = Label(registration_window, text="Client Registration", font=("Times", "16", "bold"), fg="#002D62", bg="#95F2FF", width=reduced_window_width, height=1, justify="center")
  reg_h1.place(x=0, y=10)

  reg_l1 = Label(registration_window, text="Full Name", font=("Times", "12", "bold"))
  reg_l1.place(x=20, y=50)
  entry_name = Entry(registration_window, font=("Times", "12"), width=20)
  entry_name.place(x=20 + x_gap, y=50)

  reg_l2 = Label(registration_window, text="Contact Number", font=("Times", "12", "bold"))
  reg_l2.place(x=20, y=80)
  entry_contact = Entry(registration_window, font=("Times", "12"), width=20)
  entry_contact.place(x=20 + x_gap, y=80)

  reg_l3 = Label(registration_window, text="Email", font=("Times", "12", "bold"))
  reg_l3.place(x=20, y=110)
  entry_email = Entry(registration_window, font=("Times", "12"), width=20)
  entry_email.place(x=20 + x_gap, y=110)
  email_providers = ["@gmail.com", "@outlook.com", "@yahoo.com"]
  # Datatype of email menu text
  clicked = StringVar()
  # Initial email provider selected
  clicked.set("@gmail.com")
  # Create Drop Down Menu for Email Providers
  email_drop = OptionMenu(registration_window, clicked, *email_providers)
  email_drop.place(x=320, y=110)

  reg_l4 = Label(registration_window, text="Card Number", font=("Times", "12", "bold"))
  reg_l4.place(x=20, y=140)
  entry_card_number = Entry(registration_window, font=("Times", "12"), width=20)
  entry_card_number.place(x=20 + x_gap, y=140)

  # Set character limit in Entry widgets
  entry_contact.config(validate="key", validatecommand=(root.register(limit_size(entry_contact, 11)), '%P'))
  entry_card_number.config(validate="key", validatecommand=(root.register(limit_size(entry_card_number, 13)), '%P'))

  # Server Response/Message
  reg_l5 = Label(registration_window, text="Message:", font=("Times", "12", "bold"))
  reg_l5.place(x=20, y=240)

  # Show RFID Status Message
  rfid_status = Label(registration_window, text=" ", font=("Times", "15"), width=40, height=5, justify="center", bg="#fff")
  rfid_status.place(x=100, y=240)

  # GUI Buttons
  # Registration Button/Form Submit Button
  reg_btn1 = Button(registration_window, text="Register", command=submit_registration, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  reg_btn1.place(x=20, y=190)
  
  # Clear Form Fields Button
  reg_btn2 = Button(registration_window, text="Clear", command=lambda: clear_fields(entry_name, entry_contact, entry_email, entry_card_number), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  reg_btn2.place(x=170, y=190)

  # Main Menu Button
  reg_btn3 = Button(registration_window, text="Main Menu", command=main_menu, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  reg_btn3.place(x=320, y=190)
  
  # Read RFID Button
  rfid_btn = Button(registration_window, text="Read RFID", command=lambda: read_rfid(entry_card_number, rfid_status), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  rfid_btn.place(x=470, y=140)

  # Application Exit Button
  reg_btn5 = Button(registration_window, text="Exit", command=root.quit, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  reg_btn5.place(x=470, y=190)

  show_footer(window_width, window_height)

def show_change_pin_form():
  def submit_pin_change():
    # Check if all the entries are filled
    if not validate_entries([entry_card, entry_prev_pin, entry_new_pin, entry_confirm_pin]):
      messagebox.showerror("Error", "Please fill in all the entry fields.")
      return

    # Entry Field Validation
    if not entry_prev_pin.get().isdigit() or not entry_new_pin.get().isdigit() or not entry_confirm_pin.get().isdigit():
      messagebox.showerror("Error", "Invalid ATM Pin Entries!\nPlease enter numeric values only.")
      return

    result = change_atm_pin(str(entry_card.get()), int(entry_prev_pin.get()), int(entry_new_pin.get()), int(entry_confirm_pin.get()))
    pin_l6 = Label(pin_window, text=result, font=("Times", "15"), width=40, height=5, justify="center", bg="#95F2FF")
    pin_l6.place(x=100, y=290)
    #messagebox.showinfo("Change PIN", result)
    clear_fields(entry_card, entry_prev_pin, entry_new_pin, entry_confirm_pin)
    pin_l6.after(message_timeout, lambda: pin_l6.destroy())

  # pin_window = frame
  pin_window = root

  # Set window dimensions
  window_width = 620
  window_height = 510

  # Fix GUI Window Initial Position
  x, y = window_fix_pos(pin_window, window_width, window_height)

  pin_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  clear_root()

  # Set window title
  pin_window.title("Change ATM PIN")

  x_gap = 130
  y_gap = 40

  window_width_percent = 91
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  pin_h1 = Label(pin_window, text="Change ATM PIN", font=("Times", "16", "bold"), fg="#002D62", bg="#95F2FF", width=reduced_window_width, height=1, justify="center")
  pin_h1.place(x=0, y=10)

  pin_l1 = Label(pin_window, text="Card Number", font=("Times", "12", "bold"))
  pin_l1.place(x=20, y=50)
  entry_card = Entry(pin_window, font=("Times", "12"), width=20)
  entry_card.place(x=20 + x_gap, y=50)

  pin_l2 = Label(pin_window, text="Previous PIN", font=("Times", "12", "bold"))
  pin_l2.place(x=20, y=90)
  entry_prev_pin = Entry(pin_window, show="*", font=("Times", "12"), width=20)
  entry_prev_pin.place(x=20 + x_gap, y=90)

  pin_l3 = Label(pin_window, text="New PIN", font=("Times", "12", "bold"))
  pin_l3.place(x=20, y=130)
  entry_new_pin = Entry(pin_window, show="*", font=("Times", "12"), width=20)
  entry_new_pin.place(x=20 + x_gap, y=130)

  pin_l4 = Label(pin_window, text="Confirm New PIN", font=("Times", "12", "bold"))
  pin_l4.place(x=20, y=170)
  entry_confirm_pin = Entry(pin_window, show="*", font=("Times", "12"), width=20)
  entry_confirm_pin.place(x=20 + x_gap, y=170)

  # Set character limit in Entry widgets
  entry_card.config(validate="key", validatecommand=(root.register(limit_size(entry_card, 13)), '%P'))
  entry_prev_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_prev_pin, 5)), '%P'))
  entry_new_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_new_pin, 5)), '%P'))
  entry_confirm_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_confirm_pin, 5)), '%P'))

  pin_l5 = Label(pin_window, text="Message:", font=("Times", "12", "bold"))
  pin_l5.place(x=20, y=290)

  # Show RFID Status Message
  rfid_status = Label(pin_window, text=" ", font=("Times", "15"), width=40, height=5, justify="center", bg="#fff")
  rfid_status.place(x=100, y=290)

  # GUI Buttons
  # Change PIN Button/Form Submit Button
  pin_btn1 = Button(pin_window, text="Change PIN", command=submit_pin_change, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  pin_btn1.place(x=20, y=230)

  # Clear Form Fields Button
  pin_btn2 = Button(pin_window, text="Clear", command=lambda: clear_fields(entry_card, entry_prev_pin, entry_new_pin, entry_confirm_pin), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  pin_btn2.place(x=170, y=230)

  # Main Menu Button
  pin_btn3 = Button(pin_window, text="Main Menu", command=main_menu, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  pin_btn3.place(x=320, y=230)
  
  # Read RFID Button
  rfid_btn = Button(pin_window, text="Read RFID", command=lambda: read_rfid(entry_card, rfid_status), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  rfid_btn.place(x=470, y=170)

  # Application Exit Button
  pin_btn4 = Button(pin_window, text="Exit", command=root.quit, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  pin_btn4.place(x=470, y=230)

  show_footer(window_width, window_height)

def show_balance_inquiry_form():
  def submit_balance_inquiry():
    # Check if all the entries are filled
    if not validate_entries([entry_card, entry_pin]):
      messagebox.showerror("Error", "Please fill in all the entry fields.")
      return
    
    # Entry Field Validation
    if not entry_pin.get().isdigit():
      messagebox.showerror("Error", "Invalid ATM Pin Entry!\nPlease enter numeric values only.")
      return

    result = client_balance_display(str(entry_card.get()), int(entry_pin.get()))
    balance_l4 = Label(balance_window, text=result, font=("Times", "13", "bold"), width=44, height=5, justify="center", bg="#95F2FF")
    balance_l4.place(x=100, y=280)
    #messagebox.showinfo("Balance Inquiry", result)
    clear_fields(entry_card, entry_pin)
    balance_l4.after(message_timeout, lambda: balance_l4.destroy())

  # balance_window = frame
  balance_window = root

  # Set window dimensions
  window_width = 600
  window_height = 500

  # Fix GUI Window Initial Position
  x, y = window_fix_pos(balance_window, window_width, window_height)

  balance_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  clear_root()

  # Set window title
  balance_window.title("Balance Inquiry")

  x_gap = 130
  y_gap = 40

  window_width_percent = 91
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  # Heading
  balance_h1 = Label(balance_window, text="Balance Inquiry", font=("Times", "16", "bold"), fg="#002D62", bg="#95F2FF", width=reduced_window_width, height=1, justify="center")
  balance_h1.place(x=0, y=10)

  balance_l1 = Label(balance_window, text="Card Number", font=("Times", "12", "bold"))
  balance_l1.place(x=20, y=60)
  entry_card = Entry(balance_window, font=("Times", "12", "bold"), width=20)
  entry_card.place(x=20 + x_gap, y=60)

  balance_l2 = Label(balance_window, text="ATM PIN", font=("Times", "12", "bold"))
  balance_l2.place(x=20, y=100)
  entry_pin = Entry(balance_window, show="*", font=("Times", "12"), width=20)
  entry_pin.place(x=20 + x_gap, y=100)

  # Set character limit in Entry widgets
  entry_card.config(validate="key", validatecommand=(root.register(limit_size(entry_card, 13)), '%P'))
  entry_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_pin, 5)), '%P'))


  balance_l3 = Label(balance_window, text="Message:", font=("Times", "12", "bold"))
  balance_l3.place(x=20, y=280)

  # Show RFID Status Message
  rfid_status = Label(balance_window, text=" ", font=("Times", "13"), width=48, height=5, justify="center", bg="#fff")
  rfid_status.place(x=100, y=280)

  # GUI Buttons
  # Balance Inquiry Button/Form Submit Button
  balance_btn1 = Button(balance_window, text="Check Balance", command=submit_balance_inquiry, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  balance_btn1.place(x=20, y=160)

  # Clear Form Fields Button
  balance_btn2 = Button(balance_window, text="Clear", command=lambda: clear_fields(entry_card, entry_pin), font="Helvetica 15 bold italic", width=12, cursor="hand2")
  balance_btn2.place(x=200, y=160)

  # Main Menu Button
  balance_btn3 = Button(balance_window, text="Main Menu", command=main_menu, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  balance_btn3.place(x=380, y=160)
  
  # Read RFID Button
  rfid_btn = Button(balance_window, text="Read RFID", command=lambda: read_rfid(entry_card, rfid_status), font="Helvetica 15 bold italic", width=12, cursor="hand2")
  rfid_btn.place(x=380, y=100)

  # Application Exit Button
  balance_btn4 = Button(balance_window, text="Exit", command=root.quit, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  balance_btn4.place(x=380, y=220)

  show_footer(window_width, window_height)

def show_account_details_form():
  currency_symbol = u"\u20B9" # Rupee symbol
  def submit_account_details():
    # Check if all the entries are filled
    if not validate_entries([entry_card, entry_pin]):
      messagebox.showerror("Error", "Please fill in all the entry fields.")
      return
    
    # Entry Field Validation
    if not entry_pin.get().isdigit():
      messagebox.showerror("Error", "Invalid ATM Pin Entry!\nPlease enter numeric values only.")
      return

    server_msg1, server_msg2 = view_account_details(str(entry_card.get()), int(entry_pin.get()))
    
    msg = ("Name:\t" + str(server_msg2[0]) + "\nContact Number:\t" + str(server_msg2[1]) + "\nEmail:\t" + str(server_msg2[2]) + "\nAccount Number:\t" + str(server_msg2[3]) + "\nBalance:\t" + str(currency_symbol) + str(server_msg2[4]))

    # Show Account Details
    details_msg1 = Label(details_window, text=str(server_msg2[0]), font=("Times", "12"), justify="left")
    details_msg1.place(x=170, y=220)
    details_msg2 = Label(details_window, text=str(server_msg2[1]), font=("Times", "12"), justify="left")
    details_msg2.place(x=170, y=260)
    details_msg3 = Label(details_window, text=str(server_msg2[2]), font=("Times", "12"), justify="left")
    details_msg3.place(x=170, y=300)
    details_msg4 = Label(details_window, text=str(server_msg2[3]), font=("Times", "12"), justify="left")
    details_msg4.place(x=170, y=340)
    details_msg5 = Label(details_window, text=str(server_msg2[4]), font=("Times", "12"), justify="left")
    details_msg5.place(x=170, y=380)
    #messagebox.showinfo("Account Details", msg)

    # Show Error Message if any received
    if not server_msg1 == "":
      details_error_msg1 = Label(details_window, text=server_msg1, font=("Times", "13", "bold"), justify="center", fg="#fff", bg="#FF0000")
      details_error_msg1.place(x=160, y=300)
      #messagebox.showerror("Account Details", server_msg1)
    
    # Clear all the Entry Fields of the form
    clear_fields(entry_card, entry_pin)

    # Clear Messages after a specified timeout
    details_msg1.after(message_timeout, lambda: details_msg1.destroy())
    details_msg2.after(message_timeout, lambda: details_msg2.destroy())
    details_msg3.after(message_timeout, lambda: details_msg3.destroy())
    details_msg4.after(message_timeout, lambda: details_msg4.destroy())
    details_msg5.after(message_timeout, lambda: details_msg5.destroy())
    if not server_msg1 == "":
      details_error_msg1.after(message_timeout, lambda: details_error_msg1.destroy())

  # details_window = frame
  details_window = root

  # Set window dimensions
  window_width = 600
  window_height = 510

  # Fix GUI Window Initial Position
  x, y = window_fix_pos(details_window, window_width, window_height)

  details_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  clear_root()

  # Set window title
  details_window.title("View Account Details")

  x_gap = 130
  y_gap = 40

  window_width_percent = 91
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  # Heading
  details_h1 = Label(details_window, text="View Account Details", font=("Times", "16", "bold"), fg="#002D62", bg="#95F2FF", width=reduced_window_width, height=1, justify="center")
  details_h1.place(x=0, y=10)

  details_l1 = Label(details_window, text="Card Number", font=("Times", "12", "bold"))
  details_l1.place(x=20, y=60)
  entry_card = Entry(details_window, font=("Times", "12"), width=20)
  entry_card.place(x=20 + x_gap, y=60)

  details_l2 = Label(details_window, text="ATM PIN", font=("Times", "12", "bold"))
  details_l2.place(x=20, y=100)
  entry_pin = Entry(details_window, show="*", font=("Times", "12"), width=20)
  entry_pin.place(x=20 + x_gap, y=100)
  
  # Set character limit in Entry widgets
  entry_card.config(validate="key", validatecommand=(root.register(limit_size(entry_card, 13)), '%P'))
  entry_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_pin, 5)), '%P'))

  # Server Message/Account Details Section
  details_l3 = Label(details_window, text="Name:", font=("Times", "12", "bold"))
  details_l3.place(x=20, y=220)

  details_l4 = Label(details_window, text="Contact Number:", font=("Times", "12", "bold"))
  details_l4.place(x=20, y=260)

  details_l5 = Label(details_window, text="Email:", font=("Times", "12", "bold"))
  details_l5.place(x=20, y=300)

  details_l6 = Label(details_window, text="Account Number:", font=("Times", "12", "bold"))
  details_l6.place(x=20, y=340)

  details_l7 = Label(details_window, text="Account Balance:", font=("Times", "12", "bold"))
  details_l7.place(x=20, y=380)

  # View Account Details Button/Form Submit Button
  details_btn1 = Button(details_window, text="View Details", command=submit_account_details, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  details_btn1.place(x=20, y=160)

  # Clear Form Fields Button
  details_btn2 = Button(details_window, text="Clear", command=lambda: clear_fields(entry_card, entry_pin), font="Helvetica 15 bold italic", width=12, cursor="hand2")
  details_btn2.place(x=200, y=160)

  # Main Menu Button
  details_btn2 = Button(details_window, text="Main Menu", command=main_menu, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  details_btn2.place(x=380, y=160)
  
  # Read RFID Button
  rfid_btn = Button(details_window, text="Read RFID", command=lambda: read_rfid(entry_card, None), font="Helvetica 15 bold italic", width=12, cursor="hand2")
  rfid_btn.place(x=380, y=100)

  # Application Exit Button
  details_btn3 = Button(details_window, text="Exit", command=root.quit, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  details_btn3.place(x=380, y=220)

  show_footer(window_width, window_height)

def show_deposit_form():
  def submit_deposit():
    # Check if all the entries are filled
    if not validate_entries([entry_card, entry_pin, entry_amount]):
      messagebox.showerror("Error", "Please fill in all the entry fields.")
      return
    
    # Entry Field Validation
    if not entry_pin.get().isdigit():
      messagebox.showerror("Error", "Invalid ATM Pin Entry!\nPlease enter numeric values only.")
      return

    if not entry_amount.get().isdigit():
      messagebox.showerror("Error", "Invalid Amount Entry!\nPlease enter numeric values only.")
      return

    currency_symbol = u"\u20B9" # Rupee symbol

    # Entered Amount Validation
    if int(entry_amount.get()) <=0 or int(entry_amount.get()) < 100:
      messagebox.showerror("Error", f"Minimum amount for cash deposit is {currency_symbol}100/-")
      clear_fields(entry_card, entry_pin, entry_amount)
      return

    if int(entry_amount.get()) > 100000:
      messagebox.showerror("Error", f"Maximum amount that you can deposit in a single transaction is {currency_symbol}1,00,000/-")
      clear_fields(entry_card, entry_pin, entry_amount)
      return

    result = deposit_cash(str(entry_card.get()), int(entry_pin.get()), float(entry_amount.get()))
    deposit_l5 = Label(deposit_window, text=result, font=("Times", "15", "bold"), bg="#95F2FF", width=37, height=5, justify="center")
    deposit_l5.place(x=100, y=280)
    #messagebox.showinfo("Cash Deposit", result)
    clear_fields(entry_card, entry_pin, entry_amount)
    deposit_l5.after(message_timeout, lambda: deposit_l5.destroy())

  # deposit_window = frame
  deposit_window = root

  # Set window dimensions
  window_width = 580
  window_height = 530

  # Fix GUI Window Initial Position
  x, y = window_fix_pos(deposit_window, window_width, window_height)

  deposit_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  clear_root()

  # Set window title
  deposit_window.title("Cash Deposit")
  #deposit_window.configure(bg="#95F2FF")

  x_gap = 130
  y_gap = 40

  window_width_percent = 91
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  # Heading
  deposit_h1 = Label(deposit_window, text="Cash Deposit", font=("Times", "16", "bold"), fg="#002D62", bg="#95F2FF", width=reduced_window_width, height=1, justify="center")
  deposit_h1.place(x=0, y=10)

  # Form Entry Fields
  deposit_l1 = Label(deposit_window, text="Card Number", font=("Times", "12", "bold"))
  deposit_l1.place(x=20, y=60)
  entry_card = Entry(deposit_window, font=("Times", "12"), width=20)
  entry_card.place(x=20 + x_gap, y=60)

  deposit_l2 = Label(deposit_window, text="ATM Pin", font=("Times", "12", "bold"))
  deposit_l2.place(x=20, y=100)
  entry_pin = Entry(deposit_window, show="*", font=("Times", "12"), width=20)
  entry_pin.place(x=20 + x_gap, y=100)

  deposit_l3 = Label(deposit_window, text="Amount", font=("Times", "12", "bold"))
  deposit_l3.place(x=20, y=140)
  entry_amount = Entry(deposit_window, font=("Times", "12"), width=20)
  entry_amount.place(x=20 + x_gap, y=140)

  # Set character limit in Entry widgets
  entry_card.config(validate="key", validatecommand=(root.register(limit_size(entry_card, 13)), '%P'))
  entry_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_pin, 5)), '%P'))
  entry_amount.config(validate="key", validatecommand=(root.register(limit_size(entry_amount, 7)), '%P'))

  # Server Message Section
  deposit_l4 = Label(deposit_window, text="Message:", font=("Times", "12", "bold"))
  deposit_l4.place(x=20, y=280)

  # Show RFID Status Message
  rfid_status = Label(deposit_window, text=" ", font=("Times", "15"), width=40, height=5, justify="center", bg="#fff")
  rfid_status.place(x=100, y=280)

  # GUI Buttons
  # Cash Deposit Button/Form Submit Button
  deposit_btn1 = Button(deposit_window, text="Deposit", command=submit_deposit, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  deposit_btn1.place(x=20, y=200)

  # Clear Form Fields Button
  deposit_btn2 = Button(deposit_window, text="Clear", command=lambda: clear_fields(entry_card, entry_pin, entry_amount), font="Helvetica 15 bold italic", width=12, cursor="hand2")
  deposit_btn2.place(x=200, y=200)

  # Main Menu Button
  deposit_btn3 = Button(deposit_window, text="Main Menu", command=main_menu, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  deposit_btn3.place(x=380, y=200)
  
  # Read RFID Button
  rfid_btn = Button(deposit_window, text="Read RFID", command=lambda: read_rfid(entry_card, rfid_status), font="Helvetica 15 bold italic", width=12, cursor="hand2")
  rfid_btn.place(x=380, y=80)

  # Application Exit Button
  deposit_btn4 = Button(deposit_window, text="Exit", command=root.quit, font="Helvetica 15 bold italic", width=12, cursor="hand2")
  deposit_btn4.place(x=380, y=140)

  # Show Application Footer
  show_footer(window_width, window_height)

# Function to display withdrawal form
def show_withdrawal_form():
  def submit_withdrawal():
    # Check if all the entries are filled
    if not validate_entries([entry_card, entry_pin, entry_amount]):
      messagebox.showerror("Error", "Please fill in all the entry fields.")
      return
    
    # Entry Field Validation
    if not entry_pin.get().isdigit():
      messagebox.showerror("Error", "Invalid ATM Pin Entry!\nPlease enter numeric values only.")
      return

    if not entry_amount.get().isdigit():
      messagebox.showerror("Error", "Invalid Amount Entry!\nPlease enter numeric values only.")
      return
    
    currency_symbol = u"\u20B9" # Rupee symbol

    # Entered Amount Validation
    if int(entry_amount.get()) <=0 or int(entry_amount.get()) < 200:
      messagebox.showerror("Error", f"Minimum amount for cash withdrawal is {currency_symbol}200/-")
      clear_fields(entry_card, entry_pin, entry_amount)
      return

    if int(entry_amount.get()) > 30000:
      messagebox.showerror("Error", f"Maximum amount that you can withdraw in a single transaction is {currency_symbol}30,000/-")
      clear_fields(entry_card, entry_pin, entry_amount)
      return
    
    # Check if the entered amount is a multiple of 200 or 500
    if not int(entry_amount.get()) % 200 == 0:
      if not int(entry_amount.get()) % 500 == 0:
        messagebox.showerror("Error", "Amount should be in multiples of 200 and 500 only.")
        clear_fields(entry_card, entry_pin, entry_amount)
        return

    # Perform withdrawal transaction
    result = withdraw_cash(str(entry_card.get()), int(entry_pin.get()), float(entry_amount.get()))
    withdraw_l5 = Label(withdrawal_window, text=result, font=("Times", "13", "bold"), bg="#95F2FF", width=45, height=5, justify="left")
    withdraw_l5.place(x=100, y=260)
    #messagebox.showinfo("Cash Withdrawal", result)
    clear_fields(entry_card, entry_pin, entry_amount)
    withdraw_l5.after(message_timeout, lambda: withdraw_l5.destroy())

  # withdrawal_window = frame
  withdrawal_window = root

  # Set window dimensions
  window_width = 620
  window_height = 500
  
  # Fix GUI Window Initial Position
  x, y = window_fix_pos(withdrawal_window, window_width, window_height)

  withdrawal_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  clear_root()
  
  # Set window title
  withdrawal_window.title("Cash Withdrawal")

  x_gap = 130
  y_gap = 40

  window_width_percent = 91
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  # Heading
  withdraw_h1 = Label(withdrawal_window, text="Cash Withdrawal", font=("Times", "16", "bold"), fg="#002D62", bg="#95F2FF", width=reduced_window_width, height=1, justify="center")
  withdraw_h1.place(x=0, y=10)

  # Form Entry Fields
  withdraw_l1 = Label(withdrawal_window, text="Card Number", font=("Times", "12", "bold"))
  withdraw_l1.place(x=20, y=60)
  entry_card = Entry(withdrawal_window, font=("Times", "12"), width=20)
  entry_card.place(x=20 + x_gap, y=60)

  withdraw_l2 = Label(withdrawal_window, text="ATM PIN", font=("Times", "12", "bold"))
  withdraw_l2.place(x=20, y=100)
  entry_pin = Entry(withdrawal_window, show="*", font=("Times", "12"), width=20)
  entry_pin.place(x=20 + x_gap, y=100)

  withdraw_l3 = Label(withdrawal_window, text="Amount", font=("Times", "12", "bold"))
  withdraw_l3.place(x=20, y=140)
  entry_amount = Entry(withdrawal_window, font=("Times", "12"), width=20)
  entry_amount.place(x=20 + x_gap, y=140)

  # Set character limit in Entry widgets
  entry_card.config(validate="key", validatecommand=(root.register(limit_size(entry_card, 13)), '%P'))
  entry_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_pin, 5)), '%P'))
  entry_amount.config(validate="key", validatecommand=(root.register(limit_size(entry_amount, 7)), '%P'))

  # Server Message Section
  withdraw_l4 = Label(withdrawal_window, text="Message:", font=("Times", "12", "bold"))
  withdraw_l4.place(x=20, y=260)

  # Show RFID Status Message
  rfid_status = Label(withdrawal_window, text=" ", font=("Times", "13"), width=45, height=5, justify="center", bg="#fff")
  rfid_status.place(x=100, y=260)

  # GUI Buttons
  # Cash Withdrawal Button/Form Submit Button
  withdraw_btn1 = Button(withdrawal_window, text="Withdraw", command=submit_withdrawal, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  withdraw_btn1.place(x=20, y=200)

  # Clear Form Fields Button
  withdraw_btn2 = Button(withdrawal_window, text="Clear", command=lambda: clear_fields(entry_card, entry_pin, entry_amount), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  withdraw_btn2.place(x=170, y=200)

  # Main Menu Button
  withdraw_btn3 = Button(withdrawal_window, text="Main Menu", command=main_menu, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  withdraw_btn3.place(x=320, y=200)
  
  # Read RFID Button
  rfid_btn = Button(withdrawal_window, text="Read RFID", command=lambda: read_rfid(entry_card, rfid_status), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  rfid_btn.place(x=470, y=140)

  # Application Exit Button
  withdraw_btn4 = Button(withdrawal_window, text="Exit", command=root.quit, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  withdraw_btn4.place(x=470, y=200)

  show_footer(window_width, window_height)

# Function to display Transfer Funds form
def show_transfer_funds_form():
  def submit_transfer_funds():
    # Check if all the entries are filled
    if not validate_entries([entry_card, entry_pin, entry_account, entry_amount]):
      messagebox.showerror("Error", "Please fill in all the entry fields.")
      return
    
    # Entry Field Validation
    if not entry_account.get().isdigit():
      messagebox.showerror("Error", "Invalid Account Number Entry!\nPlease enter numeric values only.")
      return
    
    if not entry_amount.get().isdigit():
      messagebox.showerror("Error", "Invalid Amount Entry!\nPlease enter numeric values only.")
      return

    if not entry_pin.get().isdigit():
      messagebox.showerror("Error", "Invalid ATM Pin Entry!\nPlease enter numeric values only.")
      return

    currency_symbol = u"\u20B9" # Rupee symbol

    # Entered Amount Validation
    if int(entry_amount.get()) <=0 or int(entry_amount.get()) < 100:
      messagebox.showerror("Error", f"Minimum amount for funds transfer is {currency_symbol}100/-")
      clear_fields(entry_card, entry_pin, entry_account, entry_amount)
      return

    if int(entry_amount.get()) > 100000:
      messagebox.showerror("Error", f"Maximum amount that you can transfer in a single transaction is {currency_symbol}1,00,000/-")
      clear_fields(entry_card, entry_pin, entry_account, entry_amount)
      return

    result = transfer_money(str(entry_card.get()), int(entry_pin.get()), int(entry_account.get()), float(entry_amount.get()))
    transfer_l6 = Label(transfer_funds_window, text=result, font=("Times", "13", "bold"), bg="#95F2FF", width=50, height=5, justify="center")
    transfer_l6.place(x=100, y=300)
    #messagebox.showinfo("Transfer Funds", result)
    clear_fields(entry_card, entry_pin, entry_account, entry_amount)
    transfer_l6.after(message_timeout, lambda: transfer_l6.destroy())
  
  # transfer_funds_window = frame
  transfer_funds_window = root

  # Set window dimensions
  window_width = 660
  window_height = 500

  # Fix GUI Window Initial Position
  x, y = window_fix_pos(transfer_funds_window, window_width, window_height)

  transfer_funds_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  clear_root()
  
  # Set window title
  transfer_funds_window.title("Transfer Funds")

  x_gap = 130
  y_gap = 40

  window_width_percent = 91
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  # Heading
  transfer_h1 = Label(transfer_funds_window, text="Transfer Funds", font=("Times", "16", "bold"), fg="#002D62", bg="#95F2FF", width=reduced_window_width, height=1, justify="center")
  transfer_h1.place(x=0, y=10)

  # Form Fields
  # Field-1
  transfer_l1 = Label(transfer_funds_window, text="Card Number", font=("Times", "12", "bold"))
  transfer_l1.place(x=20, y=60)
  entry_card = Entry(transfer_funds_window, font=("Times", "12"), width=20)
  entry_card.place(x=20 + x_gap, y=60)

  # Field-2
  transfer_l2 = Label(transfer_funds_window, text="Account Number", font=("Times", "12", "bold"))
  transfer_l2.place(x=20, y=100)
  entry_account = Entry(transfer_funds_window, font=("Times", "12"), width=20)
  entry_account.place(x=20 + x_gap, y=100)

  # Field-3
  transfer_l3 = Label(transfer_funds_window, text="Amount", font=("Times", "12", "bold"))
  transfer_l3.place(x=20, y=140)
  entry_amount = Entry(transfer_funds_window, font=("Times", "12"), width=20)
  entry_amount.place(x=20 + x_gap, y=140)

  # Field-4
  transfer_l4 = Label(transfer_funds_window, text="ATM PIN", font=("Times", "12", "bold"))
  transfer_l4.place(x=20, y=180)
  entry_pin = Entry(transfer_funds_window, show="*", font=("Times", "12"), width=20)
  entry_pin.place(x=20 + x_gap, y=180)

  # Set character limit in Entry widgets
  entry_card.config(validate="key", validatecommand=(root.register(limit_size(entry_card, 13)), '%P'))
  entry_account.config(validate="key", validatecommand=(root.register(limit_size(entry_account, 11)), '%P'))
  entry_amount.config(validate="key", validatecommand=(root.register(limit_size(entry_amount, 7)), '%P'))
  entry_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_pin, 5)), '%P'))

  # Server Message Section
  # Message Heading
  transfer_l5 = Label(transfer_funds_window, text="Message:", font=("Times", "12", "bold"))
  transfer_l5.place(x=20, y=300)

  # Show RFID Status Message
  rfid_status = Label(transfer_funds_window, text=" ", font=("Times", "13"), width=55, height=5, justify="center", bg="#fff")
  rfid_status.place(x=100, y=300)

  # Form GUI Buttons
  # Fund Transfer Button/Form Submit Button
  transfer_btn1 = Button(transfer_funds_window, text="Transfer Funds", command=submit_transfer_funds, font="Helvetica 15 bold italic", width=13, cursor="hand2")
  transfer_btn1.place(x=20, y=240)

  # Clear Form Fields Button
  transfer_btn2 = Button(transfer_funds_window, text="Clear", command=lambda: clear_fields(entry_card, entry_pin, entry_amount), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  transfer_btn2.place(x=205, y=240)

  # Main Menu Button
  transfer_btn3 = Button(transfer_funds_window, text="Main Menu", command=main_menu, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  transfer_btn3.place(x=355, y=240)
  
  # Read RFID Button
  rfid_btn = Button(transfer_funds_window, text="Read RFID", command=lambda: read_rfid(entry_card, rfid_status), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  rfid_btn.place(x=505, y=180)

  # Application Exit Button
  transfer_btn4 = Button(transfer_funds_window, text="Exit", command=root.quit, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  transfer_btn4.place(x=505, y=240)

  show_footer(window_width, window_height)

# Function to display Account Close Form
def show_delete_account_form():
  def submit_delete_form():
    # Check if all the entries are filled
    if not validate_entries([entry_card, entry_pin]):
      messagebox.showerror("Error", "Please fill in all the entry fields.")
      return
    
    # Entry Field Validation
    if not entry_pin.get().isdigit():
      messagebox.showerror("Error", "Invalid ATM Pin Entry!\nPlease enter numeric values only.")
      return

    result = delete_account(str(entry_card.get()), int(entry_pin.get()))
    delete_l6 = Label(delete_account_window, text=result, font=("Times", "13", "bold"), bg="#95F2FF", width=50, height=5, justify="left")
    delete_l6.place(x=100, y=220)
    #messagebox.showinfo("Delete Account", result)
    clear_fields(entry_card, entry_pin)
    delete_l6.after(message_timeout, lambda: delete_l6.destroy())

  # delete_account_window = frame
  delete_account_window = root

  # Set window dimensions
  window_width = 655
  window_height = 480

  # Fix GUI Window Initial Position
  x, y = window_fix_pos(delete_account_window, window_width, window_height)

  delete_account_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

  clear_root()
  
  # Set window title
  delete_account_window.title("Account Deletion")

  x_gap = 130
  y_gap = 40

  window_width_percent = 91
  reduced_window_width = int(window_width - ((window_width*window_width_percent)/100))

  # Heading
  delete_h1 = Label(delete_account_window, text="Account Deletion", font=("Times", "16", "bold"), fg="#002D62", bg="#95F2FF", width=reduced_window_width, height=1, justify="center")
  delete_h1.place(x=0, y=10)

  # Form Fields
  # Field-1
  delete_l1 = Label(delete_account_window, text="Card Number", font=("Times", "12", "bold"))
  delete_l1.place(x=20, y=60)
  entry_card = Entry(delete_account_window, font=("Times", "12"), width=20)
  entry_card.place(x=20 + x_gap, y=60)

  # Field-2
  delete_l2 = Label(delete_account_window, text="ATM PIN", font=("Times", "12", "bold"))
  delete_l2.place(x=20, y=100)
  entry_pin = Entry(delete_account_window, show="*", font=("Times", "12"), width=20)
  entry_pin.place(x=20 + x_gap, y=100)

  # Set character limit in Entry widgets
  entry_card.config(validate="key", validatecommand=(root.register(limit_size(entry_card, 13)), '%P'))
  entry_pin.config(validate="key", validatecommand=(root.register(limit_size(entry_pin, 5)), '%P'))

  # Message Heading
  delete_l3 = Label(delete_account_window, text="Message:", font=("Times", "12", "bold"))
  delete_l3.place(x=20, y=220)

  # Show RFID Status Message
  rfid_status = Label(delete_account_window, text=" ", font=("Times", "13"), width=55, height=5, justify="center", bg="#fff")
  rfid_status.place(x=100, y=220)

  # Form GUI Buttons
  # Account Deletion Button/Form Submit Button
  transfer_btn1 = Button(delete_account_window, text="Delete Account", command=submit_delete_form, font="Helvetica 15 bold italic", width=13, cursor="hand2")
  transfer_btn1.place(x=20, y=160)

  # Clear Form Fields Button
  transfer_btn2 = Button(delete_account_window, text="Clear", command=lambda: clear_fields(entry_card, entry_pin), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  transfer_btn2.place(x=205, y=160)

  # Main Menu Button
  transfer_btn3 = Button(delete_account_window, text="Main Menu", command=main_menu, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  transfer_btn3.place(x=355, y=160)
  
  # Read RFID Button
  rfid_btn = Button(delete_account_window, text="Read RFID", command=lambda: read_rfid(entry_card, rfid_status), font="Helvetica 15 bold italic", width=10, cursor="hand2")
  rfid_btn.place(x=505, y=100)

  # Application Exit Button
  transfer_btn4 = Button(delete_account_window, text="Exit", command=root.quit, font="Helvetica 15 bold italic", width=10, cursor="hand2")
  transfer_btn4.place(x=505, y=160)

  show_footer(window_width, window_height)

# Function to display Main Menu
def main_menu():
  # Set window title
  root.title("SmartBank Banking Services")
  # Set window dimensions
  window_width = 1100
  window_height = 590

  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()

  x = (screen_width // 2) - (window_width // 2)
  y = (screen_height // 2) - (window_height // 2)

  root.geometry(f"{window_width}x{window_height}+{x}+{y}")

  # Prevent window resizing
  root.resizable(False, False)

  clear_root()

  global image_references

  x_gap = 120
  y_gap = 30

  # Row-1, Column-1
  register_img = Image.open("images/icons/register.png")
  register_img_resize = register_img.resize((80, 80)) # (width, height)
  main_photo1=ImageTk.PhotoImage(register_img_resize)
  image_references.append(main_photo1)
  main_btn1 = Button(root, image=main_photo1, command=show_registration_form, cursor="hand2", border=2, borderwidth=10)
  main_btn1.place(x=70, y=40)
  main_l1 = Label(root, text="Registration", font="Helvetica 15 bold italic")
  main_l1.place(x=70 + x_gap, y=40 + y_gap)
  
  # Row-1, Column-2
  funds_img = Image.open("images/icons/funds.png")
  funds_img_resize = funds_img.resize((80, 80)) # (width, height)
  main_photo2=ImageTk.PhotoImage(funds_img_resize)
  image_references.append(main_photo2)
  main_btn2 = Button(root, image=main_photo2, command=show_balance_inquiry_form, cursor="hand2", border=2, borderwidth=10)
  main_btn2.place(x=390, y=40)
  main_l2 = Label(root, text="Balance Inquiry", font="Helvetica 15 bold italic")
  main_l2.place(x=390 + x_gap, y=40 + y_gap)
  
  # Row-1, Column-3
  account_img = Image.open("images/icons/account.png")
  account_img_resize = account_img.resize((80, 80)) # (width, height)
  main_photo3=ImageTk.PhotoImage(account_img_resize)
  image_references.append(main_photo3)
  main_btn3 = Button(root, image=main_photo3, command=show_account_details_form, cursor="hand2", border=2, borderwidth=10)
  main_btn3.place(x=710, y=40)
  main_l3 = Label(root, text="View Account Details", font="Helvetica 15 bold italic")
  main_l3.place(x=710 + x_gap, y=40 + y_gap)
  
  # Row-2, Column-1
  cash_deposit_img = Image.open("images/icons/cash_deposit.png")
  cash_deposit_img_resize = cash_deposit_img.resize((80, 80)) # (width, height)
  main_photo4=ImageTk.PhotoImage(cash_deposit_img_resize)
  image_references.append(main_photo4)
  main_btn4 = Button(root, image=main_photo4, command=show_deposit_form, cursor="hand2", border=2, borderwidth=10)
  main_btn4.place(x=70, y=190)
  main_l4 = Label(root, text="Cash Deposit", font="Helvetica 15 bold italic")
  main_l4.place(x=70 + x_gap, y=190 + y_gap)
  
  # Row-2, Column-2
  cash_withdrawal_img = Image.open("images/icons/cash_withdraw.png")
  cash_withdrawal_img_resize = cash_withdrawal_img.resize((80, 80)) # (width, height)
  main_photo5=ImageTk.PhotoImage(cash_withdrawal_img_resize)
  image_references.append(main_photo5)
  # Cash Withdrawal Menu Button
  main_btn5 = Button(root, image=main_photo5, command=show_withdrawal_form, cursor="hand2", border=2, borderwidth=10)
  main_btn5.place(x=390, y=190)
  main_l5 = Label(root, text="Cash Withdrawal", font="Helvetica 15 bold italic")
  main_l5.place(x=390 + x_gap, y=190 + y_gap)
  
  # Row-2, Column-3
  atm_pin_img = Image.open("images/icons/atm_pin.png")
  atm_pin_img_resize = atm_pin_img.resize((80, 80)) # (width, height)
  main_photo6=ImageTk.PhotoImage(atm_pin_img_resize)
  image_references.append(main_photo6)
  # Change ATM PIN  Menu Button
  main_btn6 = Button(root, image=main_photo6, command=show_change_pin_form, cursor="hand2", border=2, borderwidth=10)
  main_btn6.place(x=710, y=190)
  main_l6 = Label(root, text="Change ATM PIN", font="Helvetica 15 bold italic")
  main_l6.place(x=710 + x_gap, y=190 + y_gap)
  
  # Row-3 Column-1
  transfer_funds_img = Image.open("images/icons/funds_transfer_2.png")
  transfer_funds_img_resize = transfer_funds_img.resize((80, 80)) # (width, height)
  main_photo7 = ImageTk.PhotoImage(transfer_funds_img_resize)
  image_references.append(main_photo7)
  # Funds Transfer Menu Button
  main_btn7 = Button(root, image=main_photo7, command=show_transfer_funds_form, cursor="hand2", border=2, borderwidth=10)
  main_btn7.place(x=70, y=340)
  main_l7 = Label(root, text="Transfer Funds", font="Helvetica 15 bold italic")
  main_l7.place(x=70 + x_gap, y=340 + y_gap)

  # Row-3 Column-2
  acc_del_img = Image.open("images/icons/delete_account_2.png")
  acc_del_img_resize = acc_del_img.resize((80, 80)) # (width, height)
  main_photo8 = ImageTk.PhotoImage(acc_del_img_resize)
  image_references.append(main_photo8)
  # Account Deletion Menu Button
  main_btn8 = Button(root, image=main_photo8, command=show_delete_account_form, cursor="hand2", border=2, borderwidth=10)
  main_btn8.place(x=390, y=340)
  main_l8 = Label(root, text="Delete Account", font="Helvetica 15 bold italic")
  main_l8.place(x=390 + x_gap, y=340 + y_gap)

  # Row-3, Column-3
  exit_img = Image.open("images/icons/logout.png")
  exit_img_resize = exit_img.resize((80, 80)) # (width, height)
  main_photo9=ImageTk.PhotoImage(exit_img_resize)
  image_references.append(main_photo9)
  # Application Exit Button
  main_btn9 = Button(root, image=main_photo9, command=root.quit, cursor="hand2", border=2, borderwidth=10)
  main_btn9.place(x=710, y=340)
  main_l9 = Label(root, text="Exit", font="Helvetica 15 bold italic")
  main_l9.place(x=710 + x_gap, y=340 + y_gap)

  show_footer(window_width, window_height)

main_menu()

# Schedule a function to get the widget's position after the main event loop starts
# root.after(100, lambda: get_widget_position(main_btn1))

root.mainloop()