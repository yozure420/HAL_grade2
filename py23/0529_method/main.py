# member
#  物が持っている特性のこと
# 以下二つがある
# 　属性...アトリビュート　#他言語ではフィールドやプロパティとも言う
# 　           そのものが持つデータのこと。 #名詞
#   振る舞い...メソッド
#   　　　　そのものが持つ処理のこと

# 振る舞い(メソッド)
# [定義書式]
# def　メソッド名(self[,引数[,引数]]):
class User:
    # ここで関数を定義すればメソッドになる
    def hello(self):
        print("hello")

# メソッド呼び出し
# [呼出書式]
# インスタンス.メソッド名()

# インスタンス化
user = User()

user.hello()
# メソッド(≒関数)呼出は()が必要
# メソッド呼び出し時、定義側のselfは気にしない(selfは勝手に渡る)


class User:
    def hello(self,name):
        print(f"hello {name}")
        # 第一引数のselfはくどいけど必須
        # 第二引数以降に、任意引数を設定しておく

user = User()
user.hello("abc")


#戻り値
class User:
    def hello(self):
        return "hello!"
    
user = User()
print(user.hello())
# ちなみにreturn省略時はnoneが返却される

# メソッドは複数定義できる
class User:
    def a(self):
        print("a")
    def b(self):
        print("b")

user = User()
user.a()
user.b()

# 同一メソッド名は後方優先
# やらないけど、言語使用上動く　（スクリプト言語の特性上

class User:
    def a(self):
        print("a")
    def a(self):
        print("b")

user = User()
user.a()
