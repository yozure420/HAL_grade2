from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for('next'))

@app.route('/next')
def next():
    # クエリパラメータを取得するには、request.argsを用いる。
    # request.argsを用いる
    # 単一値の取得
    # 方法その1
    # id = request.args.get('id')
    # id = request.args.get('id2')
    # if id is None:
    #     id = 'None'
    #↑取得できなければNoneが返る。
    # return 'next'
    #Noneの場合の規定値設定も可
    # id = request.args.get('id2',default='none')

    #ちゃんとしたチェック処理を作ってみると。。。
    # id = request.args.get('id')
    # if not id:
        # return 'IDは必須'
    
    #方法その2
    id = request.args['id']
    #こっちの場合、取得できない場合はエラーとなる。
    # id = request.args['id2']
    #複数値の取得
    names = request.args.getlist('names')
    # names = request.args.getlist('names2')
    #取得するのは空のリスト
    #空チェック
    if not names:
        return '空'
    return id + ''.join(names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # 開発中は5000推奨（port 80は管理者権限が必要）