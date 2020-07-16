from flask import Flask, render_template, url_for, redirect, request
from functools import html
from models import Database

db = Database()

app = Flask(__name__)

#run the setup.py upon application start

@app.route('/', methods=['POST', 'GET'])
def register_user():
    logged_in = True
    return render_template('home.html', logged_in = False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.mathod == 'POST':
        username = html.escape(request.form.get('Username'))
        firstname = html.escape(request.form.get('Firstname'))
        lastname = html.escape(request.form.get('Lastname'))
        email = html.escape(request.form.get('Email'))
        confirm_email = html.escape(request.form.get('Confirm-email'))
        password = html.escape(request.form.get('Password'))
        confirm_password = html.escape(request.form.get('Confirm-pass'))

        #validate input and encryot password

        #add to the database
        sql_query = '''INSERT INTO USERS (Username, Firstname, Lastname, Email, Password) VALUES (?, ?, ?, ?, ?)'''
        user_info = (username, firstname, lastname, email, password, password)
        db.write_query(sql_query, user_info)
    return render_template('auth/register.html')