from flask import Flask, render_template, redirect, url_for, request,make_response
app = Flask(__name__)

@app.route('/.well-known/appspecific/com.chrome.devtools.json')
def ignore_chrome_devtools():
    return ('', 204)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0',80,True)