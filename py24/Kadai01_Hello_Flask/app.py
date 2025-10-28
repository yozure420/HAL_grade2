from flask import Flask

app = Flask(__name__)

@app.route("/") #この関数のときにこのURLを動かすよ(routing機能)この場合は、/がきたときにこのURLを動かすよって意味
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    #WEbサーバー起動
    app.run('0.0.0.0',80,debug=True)
