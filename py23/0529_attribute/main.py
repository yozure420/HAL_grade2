# 　属性...アトリビュート　#他言語ではフィールドやプロパティとも言う
# 　           そのものが持つデータのこと。 #名詞
# [定義書式]
# def __init__ (self):
#     コンストラクタで、selfを用いて定義していく
#     self.アトリビュート名1 = 初期値
#     self.アトリビュート名1 = 初期値　（必要数分OK
# self...自分・自身・自己
# ということで、インスタンス化によって出来上がったもの
# それを表すのがself

class User:
    def __init__(self):
        self.id = 0
        self.name = "no name"
        self.address = ""
        tel = "090"  #selfがないとローカル変数になる

# アトリビュート値の操作
# [利用書式]
# 　インスタンス.アトリビュート名
user = User()
user.id = 123
user.address = "東京"
print(user.id, user.name, user.address)
# print(user.tel) #telはローカル変数なので、エラーになる


# アトリビュートはコンストラクタで定義が基本
# でも、言語仕様的にはコンストラクタでなくても可能
# 　（保守性上、やらないほうがいい）
class User:
    def a(self):
        self.aaa = 0
        self.bbb = 0


user = User()
# print(user.aaa)
user.a()   #aメソッドを読んで、初めて
print(user.aaa)     #←これが動く(やらないほうがいい。 __init__でやるべき)

# また、外部からの追加も可(やらないほうがいい)
user.ccc = 999
print(user.ccc)
user.aab = "ddd"
print(user.aaa)
# アトリビュートはdelで削除できる
del user.aab
# print(user.aab) #delで削除したから出ない

# コンストラクタ引数にて初期化
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


user1 = User(100, "aaa")
user2 = User(200, "bbb")

# アトリビュートはインスタンスごとに保存される

print(user1.id)
print(user1.name)
print(user2.id)
print(user2.name)

# 保存されているデータ（アトリビュート）は自分の持ち物なので自分で使える
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")

user1 = User(100, "aaa")
user1.print_name()

# アトリビュートの利用指針
# そのものが保持し続けるべきデータがあるときのみアトリビュートとする
# 基本はローカル変数