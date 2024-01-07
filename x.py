import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from dotenv import load_dotenv
import os
from twilio.rest import Client
from fpdf import FPDF

def _email(email_send,subject,body,att=False):
    print("Executed")
    password = "wwftfvijulgjikwu"

    email_user = "amogh.out@gmail.com"
    email_password = password
    msg = MIMEMultipart()
    msg["From"] = email_user
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    if att:
        attachment = open('static/assets/pdf/output.pdf', "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename=order_receipt.pdf")
        msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, email_send, text)
    server.quit()
    print("server closed")
_email("demonthefake@gmail.com","testing","this is a test")