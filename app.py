from flask import Flask, render_template, url_for, redirect, request, flash, session
from functools import wraps
import html, secrets, bcrypt
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
        #defien an errors array
        errors = []
        #validate input and encrypt password
        validate.username(username, errors)
        validate.email(email, errors)
        validate.password(password, confirm_password, errors)
        validate.firstname_lastname(firstname, lastname,errors)
        print(errors)
            
        if not errors:
            #encrypt password  and add to database.
            salt = bcrypt.gensalt()
            password = bcrypt.hashpw(password.encode('utf-8'), salt)
            utils.register_user(username, firstname, lastname, email, password)
            #send verificatin mail.
            #flask email confirmation message
            #return 'login' page.
            return redirect(url_for('login')) 

        for error in errors:
            flash(error, 'danger')

    return render_template('auth/register.html')

@app.route('/login', methods=['POST','GET'])
def login():

    erros= []
    user_info = {
        'email' : '',
        'password' : ''
    }

    if request.method == 'POST':
        email= html.escape(request.form.get('Email'))
        user_info['password'] = html.escape(request.form.get('Password'))

        user_info['email'] = email
        print(email)

        user = utils.get_user(email)
        print('checking if user exist(debugg) : {}'.format(user))

    return render_template('auth/login.html', user_info = user_info)