# モジュールは最初にimportされた時のみ実行される
# 同じモジュールを複数回importしても一度しか実行されない
import my_module
import my_module

# importしたモジュール内で定義された変数、関数、クラスなどの
# すべてのメンバにアクセスできる
print(my_module.a)
my_module.my_func()

# fromを使ってもimportと同じようにすべて実行される
from my_module2 import my_func
my_func()

# 変数も読み込める
from my_module2 import a
print(a)