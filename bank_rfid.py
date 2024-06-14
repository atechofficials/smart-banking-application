# Smart Banking Services v1.0 RFID Functionality
# Developed By Mrinal Singh Tak
# This software/program/code is licensed under GNU GPLv3 
# (General Public License v3)
# For more details visit https://choosealicense.com/licenses/gpl-3.0/

import serial
import serial.tools.list_ports
from tkinter import END
from tkinter import messagebox
import time

rfid_reader_port = "COM16" # Change this according to your rfid reader port

# Close the rfid reader serial connection after 
# waiting/not detecting any rfid card for 5-seconds
rfid_reader_timeout = 5

# Server Message display duration in milliseconds
message_timeout = 3000 # 3-seconds

# RFID reader setup
def setup_rfid_reader(rfid_reader_port):
  try:
      ser_msg = serial.Serial(rfid_reader_port, 9600, timeout=1)
      return ser_msg
  except serial.SerialException as e:
      print(f"Serial Connection error: {e}")
      return None

# Function to read RFID card number
def read_rfid(entry_field, rfid_status=None):
#   if not rfid_status == None:
#     rfid_status.config(text="Please hold the RFID card against the reader.")
    try:
        ser_msg = setup_rfid_reader(rfid_reader_port)
        start_time = time.time()
        if ser_msg:
            ser_msg.flushInput()
            while True:
                if ser_msg.in_waiting > 0:
                    rfid_data = ser_msg.read(12).decode('utf-8').strip()
                    entry_field.delete(0, END)
                    entry_field.insert(0, rfid_data)
                    ser_msg.close()
                    if not rfid_status == None:
                        rfid_status.config(text="RFID Card Read Successfully!", bg="#00FF00")
                        rfid_status.after(message_timeout, lambda: rfid_status.config(text=" ", bg="#fff"))
                    break
                
                if time.time() - start_time > rfid_reader_timeout:
                    ser_msg.close()
        else:
            # For Debugging
            print("Error: RFID reader not connected.")
            messagebox.showerror("Error", "RFID reader not connected.")
            ser_msg.close()
            if not rfid_status == None:
                rfid_status.config(text="RFID reader not connected.", bg="#FF0000")
                rfid_status.after(message_timeout, lambda: rfid_status.config(text=" ", bg="#fff"))
    except serial.SerialException as e:
        print(f"Serial Connection error: {e}")
        messagebox.showerror("Error", "Serial Connection error.")
        if not rfid_status == None:
            rfid_status.config(text="Serial Connection error.", bg="#FF0000")
            rfid_status.after(message_timeout, lambda: rfid_status.config(text=" ", bg="#fff"))
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        ser_msg.close()