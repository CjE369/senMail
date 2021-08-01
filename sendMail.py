import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import datetime
import os, sys
import time
import random
import string
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
import yagmail
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail


__now = datetime.datetime.now()

def sendVeriyAutoMail(sender , sender_pass, reciver, subject, username):
    sender_email = sender
    receiver_email = reciver
    password = sender_pass


    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email


    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)
    e = random.randint(0,9)
    f = random.randint(0,9)
    randomLetter = random.choice(string.ascii_letters)


    code = f"{a}{b}{c}{d}{e}{f}{randomLetter}"


    html = f"""\
    <html>
    <body>
        <p>{username}<br>
            your code for {subject} is {a}{b}{c}{d}{e}{f}{randomLetter}
        </p>
    </body>
    </html>
    """

    part2 = MIMEText(html, "html")

    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    return code

def sendManualMailHTML(sender , sender_pass, reciver, subject, html_msg):
    sender_email = sender
    receiver_email = reciver
    password = sender_pass


    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email


    part2 = MIMEText(html_msg, "html")

    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def sendManualMailText(sender , sender_pass, reciver, subject, text_msg):
    sender_email = sender
    receiver_email = reciver
    password = sender_pass


    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email


    part2 = MIMEText(text_msg, "plain")

    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def mailWithAttachTEXT(sender, sender_pass, reciver, subject, body, file):
    subject_msg = subject
    body = body
    sender_email = sender
    receiver_email = reciver
    password = sender_pass

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject_msg
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    filename = file

    with open(filename, "rb") as attachment:

        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )


    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

def yagaMailWithAttach(sender, subject, reciver, file, body_txt, debug):

    receiver = reciver
    body = body_txt
    filename = file

    if debug == True:
        try:
            yag = yagmail.SMTP(sender)
            yag.send(
                to=receiver,
                subject=subject,
                contents=body,
                attachments=filename,
            )
            print(yag)
            print(yag.send)
        except Exception as e:
            print(e)
    else:
        yag = yagmail.SMTP(sender)
        yag.send(
            to=receiver,
            subject=subject,
            contents=body,
            attachments=filename,
        )

def sendGridMail(sender, reciver, subject_txt, body, sendgrid_api, debug):

    sg = sendgrid.SendGridAPIClient(
        apikey=os.environ.get(sendgrid_api)
    )
    from_email = Email(sender)
    to_email = Email(reciver)
    subject = subject_txt
    content = Content(body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    if debug == True:
        print(response.status_code)
        print(response.body)
        print(response.headers)

def yagaMail(sender, subject, reciver, file, body_txt, debug):

    receiver = reciver
    body = body_txt

    if debug == True:
        try:
            yag = yagmail.SMTP(sender)
            yag.send(
                to=receiver,
                subject=subject,
                contents=body,
            )
            print(yag)
            print(yag.send)
        except Exception as e:
            print(e)
    else:
        yag = yagmail.SMTP(sender)
        yag.send(
            to=receiver,
            subject=subject,
            contents=body,
        )