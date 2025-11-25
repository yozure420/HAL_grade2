# 02_basic_sql.py
from sqlalchemy import create_engine, text

# engineの作成(DB接続の必要情報定義)
# engine = create_engine(
#     "sqlite:///0911_sqlalchemy\\user.db",
#     echo=True,  # 裏で動作しているSQLを出力する。
# )
engine = create_engine(
    'sqlite:///f:/HAL2025/PY23/0911/0911_sqlalchemy/user.db',
    echo=True,  # 裏で動作しているSQLを出力する
    )

with engine.connect() as conn:
    # with文
    # やってることは以下
    # conn = engine.connect()
    # conn.close()を自動でやってくれる。
    sql = text("""\
CREATE TABLE IF NOT EXISTS user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name STRING,
  age INTEGER
)
    """)

    # SQL実行
    conn.execute(sql)
    conn.commit()  # 変更を確定させる。




# INSERT　サニタイジング無し
# with engine.connect() as conn:
#     sql = text("INSERT INTO user(name, age) VALUES('a', 20)")

#     # SQL実行
#     result = conn.execute(sql)
#     conn.commit()  # 変更を確定させる。

#     print(f'挿入件数:{result.rowcount}')  # 挿入件数:1




# INSERT　サニタイジング有り
# with engine.connect() as conn:
#     sql = text("INSERT INTO user(name, age) VALUES(:name, :age)")

#     # SQL実行
#     result = conn.execute(sql,{'name':'b', 'age':21})
#     conn.commit()  # 変更を確定させる。

#     print(f'挿入件数:{result.rowcount}')  # 挿入件数:1




# UPDATE
with engine.connect() as conn:
    sql = text("UPDATE user SET age = :age WHERE name = :name")

    # SQL実行
    result = conn.execute(sql,{'name':'a', 'age':22})
    conn.commit()  # 変更を確定させる。

    print(f'更新件数:{result.rowcount}')  # 更新件数:1




# DELETE
with engine.connect() as conn:
    sql = text("DELETE FROM user WHERE name = :name")

    # SQL実行
    result = conn.execute(sql,{'name':'b'})
    conn.commit()  # 変更を確定させる。

    print(f'削除件数:{result.rowcount}')  # 削除件数:1



# select
with engine.connect() as con:
    sql = text("SELECT * FROM user")
    rows = con.execute(sql)

    for row in rows:
        print(f"id: {row.id}, name: {row.name}, age: {row.age}")
