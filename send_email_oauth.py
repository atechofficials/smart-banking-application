# Smart Banking Services v1.0 Email Functionality
# Developed By Mrinal Singh Tak
# This software/program/code is licensed under GNU GPLv3 
# (General Public License v3)
# For more details visit https://choosealicense.com/licenses/gpl-3.0/

import os
#import os.path
import base64
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the scope for the Google API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Function to get the Gmail API service
def get_service():
  creds = None
  # The file token.pickle stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first time.
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
  
  # If credentials are not available or are invalid, let the user log in.
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)
  
  service = build('gmail', 'v1', credentials=creds)
  return service

# Function to send email
def send_email(to_email, subject, message):
  
  service = get_service()
  
  # Fetch the admin email from the environment variable
  from_email = os.getenv('ADMIN_EMAIL')
  if not from_email:
    raise ValueError("Admin email not set in environment variables")
  
  # Sender Email Address
  #from_email = 'anonmyousstar2018jedi@gmail.com'  # Replace with your email address

  # Create a multipart message
  msg = MIMEMultipart()
  msg['From'] = from_email
  msg['To'] = to_email
  msg['Subject'] = subject

  # Attach the message body
  body = message
  msg.attach(MIMEText(body, 'plain'))
  raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
  body = {'raw': raw}

  try:
    message = (service.users().messages().send(userId="me", body=body).execute())
    print('Message ID: %s' % message['id'])
    return message
  except Exception as error:
    print(f'An error occurred: {error}')
    return None