# インヘリタンス(継承)
# オブジェクト指向3大要素の2つめ。
# あるクラスの性質を別のクラスに引き継ぐ仕組み。
# コピペではなく、差分のみ作成することができる。

# [継承書式]
# class クラス名(継承元クラス名):

class A:
    def a(self):
        print('a')

# Aの性質(メンバ)を継承したBの定義
class B(A):
    pass

b = B()
b.a()

# Aクラスの性質をBクラスに引き継いで(継承して)いるので、
# Bクラスの持ち物にaメソッドがある。

# アトリビュートも引き継がれる

class A:
    def __init__(self):
        self.id = 0

class B(A):
    pass

b = B()
print(b.id)

# [用語]
# 継承元を特に
# ・スーパークラス
# ・上位クラス
# ・親クラス
# 継承先を特に
# ・サブクラス
# ・下位クラス
# ・子クラス
# という。

# 基本親は1つで子は複数の関係
class A:
    def a(self):
        print('a')

class B(A):
    def b(self):
        print('b')

class C(A):
    def c(self):
        print('c')

b = B()
b.a()
b.b()

c = C()
c.a()
c.c()

# オーバーライド
# 上書き。スーパークラスのメソッドをサブクラスで
# 上書きすることができる。
# ※正しくは「奪い」

class A:
    def a(self):
        print('a')

class B(A):
    pass

b = B()
b.a()

class B(A):
    # 同一メソッドを別途定義すればオーバーライドとなる
    def a(self):
        print('b')

b = B()
b.a()

# サブクラスから、スーパークラスのメソッドを呼び出せる。
# [書式]
# super().メソッド名()
class B(A):
    def b(self):
        super().a()

        # self.でも行ける
        self.a()


b = B()
b.b()

# super 実用例1)
class B(A):
    # 同一メソッドを別途定義すればオーバーライドとなる
    def a(self):
        super().a()
        print('b')

b = B()
b.a()


# super 実用例2)
class A:
    def __init__(self, id):
        self.id = id

class B(A):
    def __init__(self, name):
        self.name = name

b = B("aaa")
print(b.name)
# print(b.id) コンストラクタがオーバーライドされたのでidがない

class B(A):
    def __init__(self, id, name):
        self.id = id #親の処理のコピーは悪手
        self.name = name

b = B(0, "bbb")
print(b.id)
print(b.name)

# これで要件は満たされるが
# self.id = idは冗長。コピーはいや。
# また、たくさんアトリビュートがあったら面倒。
# superを使うことで解決できる。

class B(A):
    def __init__(self, id, name):
        # 親のコンストラクタ呼出
        super().__init__(id)
        self.name = name

b = B(0, "bbb")
print(b.id)
print(b.name)

# 継承は代々引き継げる
class A:
    def a(self):
        print(1)

class B(A):
    def b(self):
        print(2)

class C(B):
    def c(self):
        print(3)

c = C()
c.a()
c.b()
c.c()

# 多重継承が可能
# 複数の親OK
class A:
    def a(self):
        print(1)

class B:
    def b(self):
        print(2)

# 継承元として、カンマで複数指定が可能。
class C(A, B):
    def c(self):
        print(3)

c = C()
c.a()
c.b()
c.c()
