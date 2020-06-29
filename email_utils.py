import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# gmail username and app password
# EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
# EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

# use local debug server for testing
def smtpDebugServer(msg):
    """
    First, set up debugger daemon. In terminal, run:

        python3 -m smtpd -c DebuggingServer -n localhost:1025

    (any local host will do)
    """
    with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.sendmail(EMAIL_ADDRESS, 'james.gullickson@gmail.com', msg)

def sendMessageWithSMTPSSL(msg):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def buildMessage(msg, opt):
    message = EmailMessage()
    message['Subject'] = opt['subject']
    message['From'] = EMAIL_ADDRESS
    message['To'] = opt['to']
    message_content = f"""
        Sender name: {msg['firstName']} {msg['lastName']}
        Sender email: {msg['emailAddress']}
        Message: {msg['messageBody']}
    """
    message.set_content(message_content)
    return message


