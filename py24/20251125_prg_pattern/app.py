# PARGパターン
# Post Redirect Get Pattern
# POSTのままだと、更新時に不具合を起こすから、(F5等で二重にPOST送ったりする)
# Redirectして、POSTyoukyuu からGET要求に
# 変更する手法
from flask import Flask, render_template, redirect, url_for, request
# Flaskインスタンスの取得
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products/new")
def products_new():
    return render_template("products/new.html")

@app.route("/products",methods=['POST'])
def products():
    # 入力値チェック　割愛
    # DB登録処理　割愛
    import datetime
    print(datetime.datetime.now())
    return render_template("products/create_complete.html")

@app.route("/products_prg/new")
def products_prg_new():
    return render_template("products_prg/new.html")

@app.route("/products_prg",methods=['POST'])
def products_prg():
    # 入力値チェック　割愛
    # DB登録処理　割愛
    import datetime
    print(datetime.datetime.now())
    return redirect(url_for("products_prg_create_complete"))

@app.route("/products_prg_create_complete")
def products_prg_create_complete():
    # return render_template("products_prg/create_complete.html")
    return render_template('products_prg/create_complete.html')

if __name__ == "__main__":
    app.run('0.0.0.0',80,True)
