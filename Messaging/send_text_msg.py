#!/usr/bin/env/python

# Import smtplib for the sending function
import smtplib
# Import the email modules
from email.mime.text import MIMEText

# Create a simple email to be converted into a text message
msg = MIMEText("Hello")
msg["Subject"] = ""
msg["From"] = "mike.vartanian@gmail.com"
msg["To"] = "2482144561@txt.att.net"
#msg["To"] = "mike.vartanian@gmail.com"

# Send the message via our own SMPT server (sendmail)
s = smtplib.SMTP("localhost")
s.set_debuglevel(1)
s.sendmail(msg["From"], [msg["To"]], msg.as_string())
s.quit()
print "Text message sent!"
