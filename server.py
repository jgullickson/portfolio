import os
from os import path, getcwd
from flask import Flask, render_template, request, redirect, url_for
from form_utils import ContactForm, handleContactForm
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

# APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
# dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv()

app = Flask(__name__)
# app.secret_key = os.getenv('APP_SECRET_KEY')
app.secret_key = os.environ.get('APP_SECRET_KEY')

csrf = CSRFProtect()
csrf.init_app(app)

# ROUTES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/success')
def success():
    return render_template(('success.html'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        handleContactForm(request.form.to_dict())
        return redirect(url_for('success'))
    return render_template('contact.html', form=form)


if (__name__ == "__main__"):
    app.run(threaded=True, port=5000)
