import smtplib
import schedule
import time
import getpass

# Requires enabled less secure app access @ myaccount.google.com
senderEmail = input("'From' Email Address\t: ")
recipientEmail = input("'To' Email Address\t: ")
emailPassword = getpass.getpass('Email Password\t\t: ') # If not specified, default prompt is 'Password: '
message = '''\
Subject: Hello from Pewcodes!

This email is sent from Python.''' # This will be the body message, after '\n'

def sendEmail(recipientEmail):
    print('Sending Email...')
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    type(smtpObj)
    smtpObj.login(senderEmail, emailPassword)
    smtpObj.sendmail(senderEmail, recipientEmail, message)
    print('Email Sent!')

def checkAndEmail():
    sendEmail(recipientEmail)

# Sends email
# checkAndEmail()

# Sends email every 'm' minutes
m = 1
schedule.every(m).minutes.do(checkAndEmail)
print('\n' + 'Scheduled email!')
while True:
    schedule.run_pending()
    time.sleep(10)