from flask import Flask,render_template
import random
from user import User
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/randNum")
def get_randNum():
    randNum = random.randint(1,3)
    return render_template("randNum.html",randNum=randNum)

@app.route("/template")
def get_template():
    randNum = random.randint(1,3)
    return render_template("template.html", randNum=randNum)

@app.route("/randImg")
def get_randImg():
    randNum = random.randint(1,3)
    return render_template("img.html", randNum=randNum)

@app.route("/rand100")
def get_rand100():
    randNum = []
    for i in range(1,100):
         randNum.append(random.randint(1,10))
    return render_template("rand100.html", randNum=randNum)

@app.route("/rand100_2")
def get_rand100_2():
    randNum = []
    for i in range(1,100):
         randNum.append(random.randint(1,10))
    return render_template("rand100_2.html", randNum=randNum)

@app.route("/layout")
def get_layout():
    randNum = []
    for i in range(1,100):
         randNum.append(random.randint(1,10))
    return render_template("layout.html", randNum=randNum)

@app.route("/layout_inh")
def get_layout_inh():
    kuji = [
        User(1,'大吉',20000,'img/dai.png'),
        User(2,'吉',10000,'img/kichi.png'),
        User(3,'凶',5000,'img/kyo.png')
    ]
    return render_template("layout_inh.html",kuji=kuji)

@app.route("/op1")
def get_op1():
    kuji = [
        # User(1,'大吉',20000,'img/dai.png'),
        # User(2,'吉',10000,'img/kichi.png'),
        # User(3,'凶',5000,'img/kyo.png')
    ]
    return render_template("op1.html",kuji=kuji)
@app.route("/op2")
def get_op2():
    kuji = [
    ]
    return render_template("op2.html",kuji=kuji)

if __name__ == "__main__":
    app.run('0.0.0.0',80,debug=True)
