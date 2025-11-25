# コンストラクタ
# 　インスタンス化の際に動作するメソッド
# 　初期化の用途に手利用される
# [定義書式]
# def __init__(self):
class User:
    def __init__(self):
        print("コンストラクタ")

user = User()
#        ↑これでコンストラクタが動作する

# コンストラクタ　&　引数
# 　コンストラクタはメソッドなので引数を渡せる

class User:
    def __init__(self,a):
        print("コンストラクタ")

user = User(123)

# コンストラクタにてreturnは記述しない

class User:
    def __init__(self,):
        # return 1
        return #あまりないけど書くとしたらこれ

user = User()