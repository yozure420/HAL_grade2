# 03_sql_injection
from sqlalchemy import create_engine, text

# engineの作成(DB接続の必要情報定義)
engine = create_engine(
    "sqlite:///0911_sqlalchemy\\user.db",
    echo=True,  # 裏で動作しているSQLを出力する。
)
# engine = create_engine(
#     'sqlite:///f:/HAL2025/PY23/0911/0911_sqlalchemy/user.db',
#     echo=True,  # 裏で動作しているSQLを出力する
#     )


id = 2
# インジェクションコード
id = '999 or 1=1'

# select文
with engine.connect() as conn:
    # セキュリティ上、文字連結はNG！
    # sql = text(f"SELECT * FROM user WHERE id = {id}")



    # サニタイジング(無害化)するには、
    # プレースホルダ(仮置き場)(:KeyName)を使う
    sql = text("SELECT * FROM user WHERE id = :id")


    # SQL実行　第２引数にて、仮置き場に値をセットする。
    rows = conn.execute(sql, {"id": id})
    for row in rows:
        print(f'id : {row.id}, name: {row.name}, age: {row.age}')
    conn.commit()  # 変更を確定させる。


name = 'a'

# select文
with engine.connect() as conn:
    sql = text(f"SELECT * FROM user WHERE name = '{name}'")
    rows = conn.execute(sql)



    # サニタイジング(無害化)するには、
    # プレースホルダ(仮置き場)(:KeyName)を使う
    # sql = text("SELECT * FROM user WHERE id = :id")


    # SQL実行　第２引数にて、仮置き場に値をセットする。
    # rows = conn.execute(sql, {"id": id})
    for row in rows:
        print(f'id : {row.id}, name: {row.name}, age: {row.age}')
    conn.commit()  # 変更を確定させる。





name = 'a'

# select文
with engine.connect() as conn:
  # SQL文のルールとして、文字データは
    # 「シングルコーテーション(')」でくくる必要がある。
    # sql = text(f"SELECT * FROM user WHERE name='{name}'")
    # rows = con.execute(sql)
 
    # プレースホルダを利用した場合、
    # 文字データを「シングルコーテーション(')」でくくる。
    # のルールは、自動的に行うため、不要。
    # というか、くくると動かない。
    # sql = text("SELECT * FROM user WHERE name=':name'") <-これは動かない。
    sql = text("SELECT * FROM user WHERE name=:name")
    rows = conn.execute(sql, {'name': name})

    # SQL実行　第２引数にて、仮置き場に値をセットする。
    for row in rows:
        print(f'id : {row.id}, name: {row.name}, age: {row.age}')
    conn.commit()  # 変更を確定させる。