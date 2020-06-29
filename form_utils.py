from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from email_utils import buildMessage, sendMessageWithSMTPSSL
import os
from dotenv import load_dotenv
load_dotenv()

class ContactForm(FlaskForm):
    firstName = StringField('First Name', [DataRequired()])
    lastName = StringField('Last Name', [DataRequired()])
    emailAddress = StringField('Email', [DataRequired(), Email(message=('Please enter a valid email address.'))])
    messageBody = TextAreaField('Message', [DataRequired(), Length(min=4, message=('Your message is too short!'))])
    submit = SubmitField()

def handleContactForm(form):
    # options = {
    #     'to': os.getenv('DEFAULT_RECIPIENT'),
    #     'subject': os.getenv('DEFAULT_SUBJECTLINE')
    # }
    options = {
        'to': os.environ.get('DEFAULT_RECIPIENT'),
        'subject': os.environ.get('DEFAULT_SUBJECTLINE')
    }
    message = buildMessage(form, options)
    sendMessageWithSMTPSSL(message)