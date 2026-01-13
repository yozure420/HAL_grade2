# Flashメッセージ
#  1回だけ表示されるメッセージで、ページ更新がなされると消える。
#  簡単なメッセージを表示する用途で利用されている。
#  例）
# 　　ログイン画面で「IDまたはパスワードが違います。」とか、
# 　　登録画面で「登録が完了しました。」とか、
#     一覧画面で「削除しました。」とか。
#  内部的な仕組みてとしては、セッションを利用し、
#  PRGパターンと併用して用いることが一般的。
from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flash_message', methods=['GET','POST'])
def flash_message():
    if request.method == 'GET':
        return render_template('flash_message.html')
    else:
        #Flash Messageの登録
        flash('一度だけ表示')
        flash('複数メッセージOK')
        return redirect(url_for('flash_message'))

if __name__ == '__main__':
    app.run(debug=True)