from flask import Flask

app = Flask(__name__)

@app.route("/") #この関数のときにこのURLを動かすよ(routing機能)この場合は、/がきたときにこのURLを動かすよって意味
def index():
    html = '''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>index</h1>
</body>
</html>
        '''
    return html

# routeでURLを決める。
@app.route('/hello')#※先頭の/は必須(ルート)
# このURLに対応する処理を関数で定義する。
# 関数名はなんでもOK。(URLと不一致でもOK)
# ただし、ダブりはないこと。
def hello():
    return "Hello"
# 関数名をダブらせると...
# @app.route('/hello2')
# def hello():
#     return "Hello"
# AssertionError: View function mapping is overwriting an existing endpoint function: helloになる


# エンドポイント
# URLに紐づいた処理をエンドポイントと言う。
# 既定では関数名がエンドポイント名となる。
# 主に後述のurl_forにて利用する。
# また、app.routeで指定したURLのことをルール(rule)と言う。
# flask routes コマンドで確認可能
# ※app.pyが存在するディレクトリにて実行すること。


#エンドポイント名の変更
@app.route('/a',endpoint='b')
def a():
    return 'a'

# endpointを付与すれば、関数名のダブりOK
@app.route('/a2',endpoint='b2')
def a():
    return 'a2'


# endpointは、関数名のダブり他、関数名が長い場合や、
# 関数の命名規則とURLの命名規則を変えたい場合に用いる。
 
 
# データ受け取りのrule
# routeにて、<変数名>とする。
@app.route('/c/<id>') #エンドポイント名bをline46で使ってるので、bにするとエラーになるのでcにする
def c(id): #ここのidのところを<id>のidと一致させないとTypeErrorになる
    return id
#引数名は、ruleに指定した変数名と同一に

@app.route('/d/<id>/<name>')
def d(id,name):
    return id + name

# 複数のデータも受け取れる
@app.route('/c/<id>/<name>')    # 上記と同じcだけど、id/nameで区別が付くのでOK
def e(id, name):                # でもこっちはcじゃダメ。関数名の重複はNG(エンドポイント指定で回避可)
    return id + name

# コンバーター
#  受け取るデータの型を定義することができる。
@app.route('/f/<int:id>') #ここでintのみと制限する
def f(id):
    return str(id + 1) #しかしflaskでreturnできるのはstrなので(他にもあるけど)strにする

# 型が違うとNot Foundになる。
 
#[型一覧]
# string:スラッシュなしのテキスト
# int:正の整数
# float:正の浮動小数点
# path:スラッシュ付きのテキスト
# uuid:UUID

if __name__ == "__main__":
    #WEbサーバー起動
    app.run('0.0.0.0',80,debug=True)

