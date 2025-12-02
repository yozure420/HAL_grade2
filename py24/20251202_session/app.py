from flask import Flask, render_template, redirect, url_for, request,make_response
from datetime import timedelta

app = Flask(__name__)

@app.route('/.well-known/appspecific/com.chrome.devtools.json')
def ignore_chrome_devtools():
    return ('', 204)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/strat_session')
def start_session():
    return redirect(url_for('index'))

@app.route('/check_session')
def check_session():
    return redirect(url_for('index'))

@app.route('/end_session')
def check_session():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run('0.0.0.0',80,True)