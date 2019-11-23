import os
import smtplib
from podverse_admin.scripts.emailTemplate import emailTemplate, EmailTemplateObj
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendNewUserEmail(receiver):
    headerText = "How to access your Podverse Premium membership"
    paragraphText = "Click the button below to use the Reset Password form, then log into your new account."
    buttonLink = os.environ['NEW_USER_EMAIL_BUTTON_LINK']
    buttonText = "Reset Password"

    htmlString = emailTemplate(EmailTemplateObj(
        headerText,
        paragraphText,
        buttonLink,
        buttonText
    ))
    
    sendEmail(htmlString, receiver, headerText)

def sendEmail(htmlString, receiver, headerText):
    sender = os.environ['NEW_USER_EMAIL_FROM']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = headerText
    msg['From'] = sender
    msg['To'] = receiver

    htmlMimeText = MIMEText(htmlString, 'html')
    msg.attach(htmlMimeText)

    mailer_host = os.environ['MAILER_HOST']
    mailer_port = os.environ['MAILER_PORT']
    username = os.environ['MAILER_USERNAME']
    password = os.environ['MAILER_PASSWORD']

    server = smtplib.SMTP(mailer_host, mailer_port)
    server.login(username, password)
    server.sendmail(
        sender,
        receiver,
        msg.as_string()
    )

    server.quit()
