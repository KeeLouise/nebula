from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/createaccount')
def createaccount():
    return render_template('createaccount.html')
