from portfolio_pkg import app
from flask import Flask, render_template, request, redirect, url_for
from portfolio_pkg.form_utils import ContactForm, handleContactForm


# ROUTES
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

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
