from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def register_user():
    return render_template('home.html', logged_in = False)