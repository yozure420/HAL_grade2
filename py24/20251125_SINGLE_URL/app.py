# flaskでは同一エンドポイントにて以下のように構成するのが代表的
# ・GETの場合…画面を表示
# ・POSTの場合…実処理
from flask import Flask, render_template, redirect, url_for, request
# Flaskインスタンスの取得
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # request.methodでGETとPOSTの処理を分けることができる
    if request.method == 'GET':  #ここは大文字!!
        return render_template("index.html")
    else:
        id = request.form.get("id")

        # 入力チェック
        # NGなら次ページのリダイレクト
        if not id:
            return redirect(url_for("index"))
        
        # 入力チェックOKなら、DB登録。
        # その後、リダイレクト。
        # リダイレクト先としては、次の2つが一般的。
        # ・自ページ
        # ・完了ページ

        # 確認画面を設ける場合も、リダイレクトにて実装。
        # ※要セッションです。
        return "簡易登録完了"



if __name__ == "__main__":
    app.run('0.0.0.0',80,True)
