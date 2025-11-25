# 0911_sqlite
# SQLite ... 簡易RDB
# Android, MacOS, Python では
# デフォルトで組み込まれている

import sqlite3

# DB接続
con = sqlite3.connect('0911/0911_sqlite\\sample.db')

# カーソル取得
cur = con.cursor()

sql = '''\
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING
)\
'''

# SQL文の実行
cur.execute(sql)

# commitで確定
con.commit()

# insert
sql = "INSERT INTO user(name) VALUES('a')"

# SQL文の実行
cur.execute(sql)

# commitで確定
# con.commit()
con.rollback

# insert
sql = "INSERT INTO user(name) VALUES('b')"

# SQL文の実行
cur.execute(sql)

# commitで確定
# con.commit()

# rollbackでキャンセル
con.rollback

# select は、execute後、
# curを用いて、結果を取得する。

sql = "SELECT * FROM user"

# SQL文の実行
cur.execute(sql)

# 抽出系(SELECT)において、
# commitとrollbackは不要。 => SQLいじくらないから！！

# for で引っこ抜けた行数文繰り返す
for row in cur:
    print(row)
    print(f"ID = {row[0]}, Name = {row[1]}")

# やってみよう！
# 以下のフォーマットで出力！
# ID = 1, Name = a
# ID = 2, Name = a


# DB切断
con.close()