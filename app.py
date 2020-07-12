from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def register_user():
    logged_in = True
    return render_template('home.html', logged_in = False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')