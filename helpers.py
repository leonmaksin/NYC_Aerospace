import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

# Configure globals
EMAIL_PASSWORD = str(open(os.path.join("secure", "email_password.txt"), "r").read())

def sendmail(message, header, reciever):
    port = 587  # For SSL
    password = EMAIL_PASSWORD
    sender_email = "nycaerospace@gmail.com"
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = reciever
    msg["Subject"] = header
    msg.attach(MIMEText(message, "html"))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()
