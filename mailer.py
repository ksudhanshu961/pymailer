#!/usr/bin/env python3

import smtplib
from email import encoders
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
import getpass


servs = smtplib.SMTP('smtp.gmail.com', 587)

servs.ehlo()
servs.starttls()
servs.ehlo()

email = str(input("\nEnter your Email address : "))
passwd = getpass.getpass("\nEnter your Password : ")

try:
    servs.login(email, passwd)

    msgs = MIMEMultipart()
    msgs['From'] = input("\nYour Name : ")
    targetmail = msgs['To'] = input("\nEnter Recipient Mail : ")
    msgs['Subject'] = input('\nEnter Subject : ')
		
    msg = 'Test'
    msgs.attach(MIMEText(msg, 'plain'))

    text = msgs.as_string()
    servs.sendmail(email, targetmail, text)

except:
    print("Server Error, Try again or use another Mail-Service")
