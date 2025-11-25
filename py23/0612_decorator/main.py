# デコレーター
# 関数（メソッド）の前後に任意処理を追加することができる
# [定義例]  ※覚えなくておｋ

def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 前処理
        print(1)
        # 実関数呼び出し
        result = func(*args, **kwargs)
        # 後処理
        print(2)
        return result
    return wrapper

# [利用書式]
# @デコレーター名
# def 関数名():

@my_decorator
def a():
    print(1)

a()