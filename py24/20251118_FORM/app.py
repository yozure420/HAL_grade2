from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
#postを受け取るには、methodの指定が必須
@app.route('/comfirm',methods=['post']) #送信ボタンをおすとメソッド送信許可がされてないので、エラーになるが、URLを直接入れてEnter押すとgetリクエストのみで走るので、confirmがでる。メソッド送信許可のためには,methods=['post']が必要
def confirm():
    #Formデータは、request.formから取得する
    #※全般request.argsと一緒。
    #フォームデータ(単一値)の取得
    id = request.form.get('id')

    #必須チェック(Noneや、空の場合があるので)
    if not id:
        return 'ID必須' #本来はリダイレクト
    

    #フォームデータ(複数値)の取得
    check = request.form.getlist('')
    #空チェック
    if not check:
        pass
    #エラーとする場合にはエラー処理を。
    return render_template('confirm.html')

if __name__ == '__main__':
    app.run('0.0.0.0',80,True)