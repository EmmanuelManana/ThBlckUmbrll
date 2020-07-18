from flask import Flask, render_template, url_for, redirect, request, flash
from functools import wraps
import html
from models import Database
from validate import Validate
import utils as utils


validate = Validate()
db = Database()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kueghfo734yfo8g387'

#run the setup.py upon application start

@app.route('/', methods=['POST', 'GET'])
def register_user():
    logged_in = True
    return render_template('home.html', logged_in = False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = html.escape(request.form.get('Username'))
        firstname = html.escape(request.form.get('Firstname'))
        lastname = html.escape(request.form.get('Lastname'))
        email = html.escape(request.form.get('Email'))
        confirm_email = html.escape(request.form.get('Cemail'))
        password = html.escape(request.form.get('Password'))
        confirm_password = html.escape(request.form.get('Confirm-pass'))

        #errors array
        errors = []
        #validate input and encrypt password
        validate.username(username, errors)
        print(errors)
            
        if not errors:
            utils.register_user(username, firstname, lastname, email, password)
            # return redirect(url_for('/'))
            return render_template('home.html') # render the gome page for sake of testing

        for error in errors:
            flash(error, 'danger')
        #add to the database
        
    return render_template('auth/register.html')