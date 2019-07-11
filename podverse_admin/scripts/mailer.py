import os
import smtplib
from podverse_admin.scripts.emailTemplate import emailTemplate, EmailTemplateObj
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

headerText = "Your Podverse Premium membership has been activated"

def sendNewUserEmail(receiver):
    #    preheader displays as preview text in some email clients
    preheader = headerText
    greeting = "Hello!"
    topMessage = headerText + ". To log into your account, click the button below, reset your password, then login."
    button = "Reset Password"
    buttonLink = os.environ['NEW_USER_EMAIL_BUTTON_LINK']
    bottomMessage = "Please let us know if there is anything we can improve."
    closing = "Thank you :)"
    name = "Podverse"
    address = "Chicago, IL, USA"
    unsubscribeLink = ""
    buttonColor = "#2968B1"
    title = headerText

    htmlString = emailTemplate(EmailTemplateObj(
        preheader,
        greeting,
        topMessage,
        button,
        buttonLink,
        bottomMessage,
        closing,
        name,
        address,
        unsubscribeLink,
        buttonColor,
        title
    ))
    
    sendEmail(htmlString, receiver)

def sendEmail(htmlString, receiver):
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
