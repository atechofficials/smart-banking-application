# Smart Banking Services v1.0 Functions
# Developed By Mrinal Singh Tak
# This software/program/code is licensed under GNU GPLv3 
# (General Public License v3)
# For more details visit https://choosealicense.com/licenses/gpl-3.0/

import sqlite3
import random
from send_email_oauth import send_email

#from bank_gui import show_change_atm_pin_form

# Function to connect to SQLite database
def connect_to_db():
  # Connect to SQLite database
  database_connect = sqlite3.connect("bank_database.db")

  # Create a cursor object
  cursor = database_connect.cursor()
  return database_connect, cursor

# Function to create table in database if not exists
def create_table():
  database_connect, cursor = connect_to_db()
  # Create table in database if not exists
  cursor.execute('''CREATE TABLE IF NOT EXISTS bank_accounts 
                    (id INTEGER PRIMARY KEY, client_name TEXT NOT NULL, contact_number INTEGER NOT NULL, email TEXT NOT NULL, account_number INTEGER NOT NULL, card_number TEXT NOT NULL, atm_pin INTEGER NOT NULL, balance REAL NOT NULL, is_temp_pin INTEGER NOT NULL)''')

  # Commit the transaction
  database_connect.commit()

  # Close the connection
  database_connect.close()

# Function to check if card number exists in database
def check_card_exists(card_number):
  database_connect, cursor = connect_to_db()

  # Check if card_number exists in database
  cursor.execute('''SELECT card_number FROM bank_accounts WHERE card_number = ?''', (card_number,))
  result = cursor.fetchone()
  # Close the connection
  database_connect.close()
  return result is not None

# Function to check if account number exists in database
def check_account_exists(account_number):
  database_connect, cursor = connect_to_db()

  # Check if account_number exists in database
  cursor.execute('''SELECT account_number FROM bank_accounts WHERE account_number = ?''', (account_number,))
  result = cursor.fetchone()
  # Close the connection
  database_connect.close()
  return result is not None

# Function to register a new client
def client_reg(name, contact, email, card_number):
  try:
    if check_card_exists(card_number):
      return "Card Number already exists. Please try again."
  
    client_name = name
    client_contact = contact
    client_email = email
    client_account_number = random.randint(1000000000, 9999999999)
    client_atm_pin = random.randint(1000, 9999)
    client_balance = 0.00

    database_connect, cursor = connect_to_db()

    # Insert data in to the table
    cursor.execute('''INSERT INTO bank_accounts (client_name, contact_number, email, account_number, card_number, atm_pin, balance, is_temp_pin) VALUES (?, ?, ?, ?, ?, ?, ?, 1)''', (client_name, client_contact, client_email, client_account_number, card_number, client_atm_pin, client_balance))
    
    # Commit the transaction
    database_connect.commit()
    
    # Close the connection
    database_connect.close()

    # Send email notification
    subject = "Welcome to SmartBank"
    message = f"Dear {client_name},\n\nWelcome to SmartBank! Your account has been created successfully. Your account number is {client_account_number} and your temporary ATM PIN is {client_atm_pin}. Please change your ATM pin as soon as possible.\n\nThank you for choosing SmartBank.\n\nBest regards,\nSmartBank Team"
    
    send_email(client_email, subject, message)

    return f"Registration Successful.\nYour Account Number is: {client_account_number}.\nYour Temporary ATM PIN is: {client_atm_pin}.\nPlease change your ATM pin as soon as possible."
  except ValueError:
    return "Invalid Input. Please enter numeric values for card number and contact number."

# Function to check account balance
def client_balance_display(card_number, atm_pin):
  try:
    if not check_card_exists(card_number):
      return "Card Number does not exist. Please try again."
    
    database_connect, cursor = connect_to_db()
    cursor.execute('''SELECT atm_pin, balance, is_temp_pin FROM bank_accounts WHERE card_number = ?''', (card_number,))
    result = cursor.fetchone()
    
    # Close the connection
    database_connect.close()

    if result is None:
      return "Card Number does not exist. Please try again."

    retrieved_atm_pin, retrieved_balance, is_temp_pin = result

    if atm_pin == retrieved_atm_pin:
      if is_temp_pin:
        return "Please change your temporary ATM PIN before proceeding."
      else:
        currency_symbol = u"\u20B9" # Rupee symbol
        return f"Your account balance is: {currency_symbol}{retrieved_balance}/-"
    else:
      return "Invalid ATM PIN. Please try again."
  except ValueError:
    return "Invalid Input. Please enter numeric values for Card Number and ATM PIN."

# Function to view Account Details
def view_account_details(card_number, atm_pin):
  try:
    msg1 = ""
    msg2 = ["", "", "", "", ""]
    if not check_card_exists(card_number):
      msg1 = "Card Number does not exist. Please try again."
      return msg1, msg2

    database_connect, cursor = connect_to_db()
    cursor.execute('''SELECT atm_pin, client_name, contact_number, email, account_number, balance, is_temp_pin FROM bank_accounts WHERE card_number = ?''', (card_number, ))
    result = cursor.fetchone()

    # Close the connection
    database_connect.close()

    if result is None:
      msg1 = "Invalid Card Number or ATM PIN. Please try again."
      return msg1, msg2

    retrieved_atm_pin, client_name, contact_number, email, account_number, balance, is_temp_pin = result

    if atm_pin == retrieved_atm_pin:
      if is_temp_pin:
        msg1 = "Please change your temporary ATM PIN before proceeding."
        return msg1, msg2
      else:
        msg2 = [client_name, contact_number, email, account_number, balance]
        return msg1, msg2
    else:
      msg1 = "Invalid ATM PIN. Please try again."
      return msg1, msg2
  except ValueError:
    msg1 = "Invalid Input. Please enter numeric values\nfor Card Number and ATM PIN."
    return msg1, msg2

# Function to deposit cash
def deposit_cash(card_number, atm_pin, deposit_amount):
  try:
    if not check_card_exists(card_number):
      return "Card Number does not exist. Please try again."

    database_connect, cursor = connect_to_db()
    cursor.execute('''SELECT atm_pin, balance, is_temp_pin, client_name, email FROM bank_accounts WHERE card_number = ?''', (card_number, ))
    result = cursor.fetchone()

    # Close the connection
    database_connect.close()

    if result is None:
      return "Invalid Card Number or ATM PIN. Please try again."

    retrieved_atm_pin, retrieved_balance, is_temp_pin, client_name, client_email = result

    if atm_pin == retrieved_atm_pin:
      if is_temp_pin:
        return "Please change your temporary ATM PIN before proceeding."
      else:
        if deposit_amount <= 0:
          return "Invalid amount entered. Please try again."

        new_balance = retrieved_balance + deposit_amount

        database_connect, cursor = connect_to_db()

        cursor.execute('''UPDATE bank_accounts SET balance = ? WHERE card_number = ?''', (new_balance, card_number))

        # Commit the transaction
        database_connect.commit()

        # Close the connection
        database_connect.close()

        currency_symbol = u"\u20B9" # Rupee symbol

        # Send email notification
        subject = "Cash Deposit Successful"
        message = f"Dear {client_name},\n\nYour cash deposit of {currency_symbol}{deposit_amount}/- has been successful. Your updated account balance is {currency_symbol}{new_balance}/-\n\nThank you for choosing SmartBank.\n\nBest regards,\nSmartBank Team"
        send_email(client_email, subject, message)

        # return "Cash deposited successfully.\nNew balance is: INR {:.2f}".format(new_balance)
        return f"Cash deposited successfully.\nYour updated account balance is: {currency_symbol}{new_balance}/-"
    else:
      return "Invalid Card Number or ATM PIN. Please try again."
  except ValueError:
    return "Invalid Input. Please enter numeric values for Card Number, ATM PIN, and Deposit Amount."

# Function to withdraw cash
def withdraw_cash(card_number, atm_pin, withdrawal_amount):
  try:
    if not check_card_exists(card_number):
      return "Card Number does not exist. Please try again."

    database_connect, cursor = connect_to_db()
    cursor.execute('''SELECT atm_pin, balance, is_temp_pin, client_name, email FROM bank_accounts WHERE card_number = ?''', (card_number, ))
    result = cursor.fetchone()

    # Close the connection
    database_connect.close()

    if result is None:
      return "Invalid Card Number or ATM PIN. Please try again."
  
    retrieved_atm_pin, retrieved_balance, is_temp_pin, client_name, client_email = result

    if atm_pin == retrieved_atm_pin:
      if is_temp_pin:
        return "Please change your temporary ATM PIN before proceeding."
      else:
        if withdrawal_amount <= 0:
          return "Invalid amount entered. Please try again."
        if withdrawal_amount > retrieved_balance:
          return "Insufficient balance. Please try again."

        new_balance = retrieved_balance - withdrawal_amount

        database_connect, cursor = connect_to_db()

        cursor.execute('''UPDATE bank_accounts SET balance = ? WHERE card_number = ?''', (new_balance, card_number))

        # Commit the transaction
        database_connect.commit()

        # Close the connection
        database_connect.close()

        currency_symbol = u"\u20B9" # Rupee symbol

        # Send email notification
        subject = "Cash Withdrawal Successful"
        message = f"Dear {client_name},\n\nYour cash withdrawal of {currency_symbol}{withdrawal_amount}/- has been successful. Your updated account balance is {currency_symbol}{new_balance}/-\n\nThank you for choosing SmartBank.\n\nBest regards,\nSmartBank Team"
        send_email(client_email, subject, message)

        #return "Cash withdrawn successfully. New balance is: INR {:.2f}".format(new_balance)
        return f"Cash withdrawn successfully.\nYour updated account balance is: {currency_symbol}{new_balance}/-"
    else:
      return "Invalid Card Number or ATM PIN. Please try again."
  except ValueError:
    return "Invalid Input. Please enter numeric values for Card Number, ATM PIN, and Withdrawal Amount."

# Function to change ATM PIN
def change_atm_pin(card_number, prev_atm_pin, new_atm_pin, confirm_atm_pin):
  try:
    database_connect, cursor = connect_to_db()
    cursor.execute('''SELECT atm_pin, client_name, email FROM bank_accounts WHERE card_number = ?''', (card_number,))
    result = cursor.fetchone()

    if result is None or prev_atm_pin != result[0]:
      # Close the connection
      database_connect.close()
      return "Invalid Card Number or ATM PIN. Please try again."

    if new_atm_pin != confirm_atm_pin:
      return "ATM PIN does not match. Please try again."
  
    cursor.execute('''UPDATE bank_accounts SET atm_pin = ?, is_temp_pin = 0 WHERE card_number = ?''', (new_atm_pin, card_number))

    # Commit the transaction
    database_connect.commit()

    # Close the connection
    database_connect.close()

    # Send email notification
    client_name = result[1]
    client_email = result[2]
    subject = "ATM PIN Changed"
    message = f"Dear {client_name},\n\nYour ATM PIN has been changed successfully. If this is not you, please contact us immediately.\n\nThank you for choosing SmartBank.\n\nBest regards,\nSmartBank Team"
    send_email(client_email, subject, message)

    return "ATM PIN changed successfully."
  except ValueError:
    return "Invalid Input. Please enter numeric values for ATM pin."

# Function to verify ATM Pin
def verify_atm_pin(card_number, atm_pin):
  try:
    if not check_card_exists(card_number):
      # For Debugging
      print("verify_atm_pin() function Error: Card Number does not exist. Please try again.")
      return False

    database_connect, cursor = connect_to_db()
    cursor.execute('''SELECT atm_pin FROM bank_accounts WHERE card_number = ?''', (card_number,))
    result = cursor.fetchone()

    # Close the connection
    database_connect.close()

    if result is None:
      # For Debugging
      print("verify_atm_pin() function Error: Invalid Card Number or ATM PIN. Please try again.")
      return False

    # retrieved_atm_pin = result

    # if atm_pin == retrieved_atm_pin:
    #   return True

    return result and result[0] == atm_pin

  except ValueError:
    # For Debugging
    print("verify_atm_pin() function Error: Invalid Input. Please enter numeric values for Card Number and ATM PIN.")

# Function to transfer funds to another account
def transfer_money(sender_card, sender_pin, receiver_account, amount):
  try:
    if not check_card_exists(sender_card):
      return "Your Card Number does not exist or Invalid.\nPlease try again."

    if str(receiver_account) == str(sender_card):
      return "You cannot transfer funds to yourself.\nPlease try again."
    
    if not check_account_exists(receiver_account):
      return "Receiver's Account Number does not exist or Invalid.\nPlease try again."

    if not verify_atm_pin(sender_card, sender_pin):
      return "Invalid Card Number or ATM PIN.\nPlease try again."
    
    # Conntect to database
    database_connect, cursor = connect_to_db()
    
    # Fetch Sender's temporary ATM Pin status, balance, name and email from database
    cursor.execute('''SELECT is_temp_pin, balance, client_name, email, account_number FROM bank_accounts WHERE card_number = ?''', (sender_card,))
    sender_acc_details = cursor.fetchone()

    if sender_acc_details is None:
      # Close the database connection
      database_connect.close()
      return "Invalid Card Number. Please try again."

    is_temp_pin = sender_acc_details[0]

    if is_temp_pin:
      # Close the database connection
      database_connect.close()
      return "Please change your temporary ATM PIN before proceeding."

    sender_balance = sender_acc_details[1]
    if not sender_balance or sender_balance < amount:
      # Close the database connection
      database_connect.close()
      return "Insufficient balance in your account.\nPlease try again."
    
    sender_name = sender_acc_details[2]
    sender_email = sender_acc_details[3]
    sender_account_number = sender_acc_details[4]

    # Fetch receiver's balance from database
    cursor.execute('''SELECT balance, client_name, email FROM bank_accounts WHERE account_number = ?''', (receiver_account,))
    receiver_acc_details = cursor.fetchone()

    if not receiver_acc_details:
      # Close the database connection
      database_connect.close()
      return "Receiver Account Number does not exist or Invalid.\nPlease try again."
    
    receiver_name = receiver_acc_details[1]
    receiver_email = receiver_acc_details[2]

    receiver_balance = receiver_acc_details[0]

    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount

    # Update sender's balance in database
    cursor.execute('''UPDATE bank_accounts SET balance = ? WHERE card_number = ?''', (new_sender_balance, sender_card))

    # Update receiver's balance in database
    cursor.execute('''UPDATE bank_accounts SET balance = ? WHERE account_number = ?''', (new_receiver_balance, receiver_account))

    # Commit Changes
    database_connect.commit()

    # Close the database connection
    database_connect.close()

    currency_symbol = u"\u20B9" # Rupee symbol

    # Send email notification to sender
    subject = "Funds Transfered Successfully"
    message = f"Dear {sender_name},\n\nYour funds transfer of {currency_symbol}{amount}/- to {receiver_name} with account number: {receiver_account} has been successful. Your updated account balance is {currency_symbol}{new_sender_balance}/-\n\nThank you for choosing SmartBank.\n\nBest regards,\nSmartBank Team"
    
    send_email(sender_email, subject, message)

    # Send email notification to receiver
    subject = "Funds Received"
    message = f"Dear {receiver_name},\n\nYou have received {currency_symbol}{amount}/- from {sender_name} with account number: {sender_account_number}. Your updated account balance is {currency_symbol}{new_receiver_balance}/-\n\nThank you for choosing SmartBank.\n\nBest regards,\nSmartBank Team"

    send_email(receiver_email, subject, message)

    return f"{currency_symbol}{amount}/- transferred successfully\n to {receiver_name} with account number: {receiver_account}.\nYour updated balance is {currency_symbol}{new_sender_balance}/-"
  except ValueError:
    return "Invalid Input. Please enter numeric values for Card Number,\nATM PIN, Receiver's Account Number, and Amount."

# Function to delete/close bank account
def delete_account(card_number, atm_pin):
  try:
    if not check_card_exists(card_number):
      return "Card Number does not exist. Please try again."

    if not verify_atm_pin(card_number,atm_pin):
      return "Invalid Card Number or ATM PIN. Please try again."

    # Connect to database
    database_connect, cursor = connect_to_db()
    cursor.execute('''SELECT is_temp_pin, balance, client_name, email, account_number FROM bank_accounts WHERE card_number = ?''', (card_number,))
    account_detials = cursor.fetchone()

    if account_detials is None:
      # Close the connection
      database_connect.close()
      return "Invalid Card Number or ATM PIN. Please try again."

    temp_atm_pin_status, client_balance, client_name, client_email, client_account_number = account_detials

    if temp_atm_pin_status:
      # Close the database connection
      database_connect.close()
      return "Please change your temporary ATM PIN before proceeding."

    if int(client_balance) != 0 or int(client_balance) > 0:
      # Close the database connection
      database_connect.close()
      return "You have funds in your account.\nPlease withdraw your funds before closing your bank account."

    # Delete the account from database
    cursor.execute('''DELETE FROM bank_accounts WHERE card_number = ?''', (card_number,))

    # Commit the changes to database
    database_connect.commit()

    # Close the database connection
    database_connect.close()
    
    # Send email notification
    subject = "Bank Account Closed"
    message = f"Dear {client_name},\n\nYour SmartBank account with account number: {client_account_number} has been closed successfully. We are sorry to see you go.\n\nThank you for choosing SmartBank.\n\nBest regards,\nSmartBank Team"

    send_email(client_email, subject, message)

    return f"Dear {client_name}, your SmartBank account with\n account number: {client_account_number} has been closed successfully."

  except ValueError:
    return "Invalid Input. Please enter numeric values for Card Number and ATM PIN."