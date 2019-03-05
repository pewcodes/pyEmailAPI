import smtplib
import schedule
import time
import getpass

# Requires enabled less secure app access @ myaccount.google.com
senderEmail = input("'From' Email Address\t: ")
recipientEmail = input("'To' Email Address\t: ")
emailPassword = getpass.getpass('Email Password\t\t: ') # If not specified, default prompt is 'Password: '
subject = input('Subject\t\t\t: ')
msg = input('Message\t\t\t: ')
message = 'Subject: ' + subject + '\n\n' + msg


def sendEmail(recipientEmail):
    print('\n' + 'Sending Email...')
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    type(smtpObj)
    smtpObj.login(senderEmail, emailPassword)
    smtpObj.sendmail(senderEmail, recipientEmail, message)
    print('Email Sent!')

def checkAndEmail():
    sendEmail(recipientEmail)


interval = input('''Interval in minutes 
(immediate by default)\t: ''')

if interval == '':
    checkAndEmail()
else:
    # Sends email every 'i' minutes
    i = int(interval)
    schedule.every(i).minutes.do(checkAndEmail)
    print('Scheduled email!' + ' Sending email every ' + interval + ' minute(s).')
    while True:
        schedule.run_pending()
        time.sleep(10)