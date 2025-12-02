# Cookie
#  クライアントサイドに情報を残す技術。
#
# [仕組み]
#  ①サーバーサイドにて、HTTPレスポンスヘッダに、key=valueの形でデータを積む。
#  ②クライアント(ブラウザ)にて、key=valueを保存する。
#  ③サーバーに再要求(リクエスト)時、key=valueをHTTPリクエストヘッダに積む。
#  ④サーバーサイドにて、keyを指定してデータを引っこ抜く。※①のvalueを復元することができる。
# [Point!]
#  クライアントサイドに保存された情報は、再リクエスト時に自動的に送信される。
# [注意事項]
#  データサイズに上限がある。約4KB。
#  データ漏洩の危険性がある。(機密情報は保持しない様にする。)
# [用途]
#  ・セッション管理…セッションIDを保存し、繋がっている状態を実現する。
#  ・設定情報の保存…ユーザーの設定情報を保存し、次回に適用する。
#  ・トラッキング…ユーザーのブラウジング行動を保存し、追跡出来るようにする。
#  ・CRRF対策 等々。
from flask import Flask, render_template, redirect, url_for, request,make_response
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/set_cookie')
def set_cookie():
    # レスポンスオブジェクト(イメージHTTPパケット)を生成する
    response = make_response(redirect(url_for('index')))
    return response

if __name__ == "__main__":
    app.run('0.0.0.0',80,True)