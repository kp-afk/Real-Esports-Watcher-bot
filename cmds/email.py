import discord
from discord.ext import commands
import variables
import random
import os
import pymongo
from pymongo import MongoClient
import smtplib, ssl
from cryptography.fernet import Fernet
import discord
from discord.ext import commands
import random
import os
import pymongo
from pymongo import MongoClient
import smtplib, ssl
import httplib2
import os
import oauth2client
from oauth2client import client, tools, file
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery
import mimetypes
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import httplib2
import os
import oauth2client
from oauth2client import client, tools
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery

CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Send Email'
SCOPES = 'https://www.googleapis.com/auth/gmail.send'
key = os.getenv('key')


def get_credentials():
    fernet = Fernet(key)
    with open('gmail-python-email-send.json', 'rb') as enc_file:
      encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('gmail-python-email-send.json', 'wb') as dec_file:
      dec_file.write(decrypted)
    with open('client_secret.json', 'rb') as enc_file:
      encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('client_secret.json', 'wb') as dec_file:
      dec_file.write(decrypted)
# ---------------------------------------------------------------
    credential_path = 'gmail-python-email-send.json'
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
# --------------------------------------------------------------
    with open('gmail-python-email-send.json', 'rb') as file:
      original = file.read()
    encrypted = fernet.encrypt(original)
    with open('gmail-python-email-send.json', 'wb') as encrypted_file:
      encrypted_file.write(encrypted)
      return credentials
    with open('client_secret.json', 'rb') as file:
      original = file.read()
    encrypted = fernet.encrypt(original)
    with open('client_secret.json', 'wb') as encrypted_file:
      encrypted_file.write(encrypted)
      return credentials

def SendMessage(sender, to, subject, msgHtml, msgPlain):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message1 = CreateMessage(sender, to, subject, msgHtml, msgPlain)
    SendMessageInternal(service, "me", message1)

def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

def CreateMessage(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    return body

def main():
    to = "to@address.com"
    sender = "from@address.com"
    subject = "subject"
    msgHtml = "Hi<br/>Html Email"
    msgPlain = "Hi\nPlain Email"
    SendMessage(sender, to, subject, msgHtml, msgPlain)

if __name__ == '__main__':
    main()
