# 05_orm.py

from sqlalchemy import create_engine, String, func, asc, desc
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from typing import Optional

# engineの作成(DB接続の必要情報定義)
engine = create_engine(
    'sqlite:///0911_sqlalchemy\\user2.db',
#     'sqlite:///f:/HAL2025/PY23/0911/0911_sqlalchemy\\user2.db',
    echo=True
)

# モデルの元クラスを作成
class Base(DeclarativeBase):
    pass

# Baseクラスを継承して、
# テーブル用のクラスを定義する。
class User(Base):
    __tablename__ = 'user'
 
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20))
    age: Mapped[int]    # 特に指定がなければmapped_columnは不要。※= Columnは古い。
    address: Mapped[Optional[str]]  # Optionalでnull許容（defaultはNOT NULL）
 
    # memo:実際に実行されるCREATE文に AUTO INCREMENT の記載がないが、
    # 問題はない。これは、SQLiteが、INTのPRIMARY KEYは自動的に
    # AUTO INCREMENTの扱いになるという仕様による。
    # なので、「, autoincrement=True」自体も不要だが、
    # もし自動採番したくない場合には、これをFalseとする必要がある。

# テーブルの作成
Base.metadata.create_all(bind=engine)


# 登録
# with Session(engine) as session:
#    user = User(name = 'a', age = 20, address=None)
#    session.add(user)
#    session.commit()

# 登録
# with Session(engine) as session:
#    user = User(name = 'b', age = 25, address='神奈川')
#    session.add(user)
#    session.commit()

# 抽出
with Session(engine) as session:
  #  session.queryを使って一行ずつ取得する。
  for user in session.query(User):
     print(user.id, user.name, user.age, user.address)


# .all()付与で、全件取得
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age, user.address)

    # .all()あり→全件一括取得＝スピード〇、メモリ×
    #  →usersの形で、別のプログラムに受け渡すときに使う（ほぼこっち）。
    # .all()なし→１行ずつ取得＝スピード×、メモリ〇
    #　→データ量がものすごい多い（何千、何万の）ときに使う。

    # .firest で、最初の1件だけ取得
    user = session.query(User).first()
    print(user.id, user.name, user.age, user.address)
    # 0件の場合はNoneのため、ガチガチに組むなら、if user:といったチェック処理が必要。

    # .scalar()でスカラー(単一)値取得
    count = session.query(func.count(User.id))
    print(count)

    #COUNT(*)は↓
    count = session.query(func.count('*')).select_from(User).scalar()
    print(count)

    # .limit()で取得件数絞り込み
    users = session.query(User).limit(2).all()
    #.allじゃなくてもOKだけど、つけるなら.allは最後
    for user in users:
        print(user.id, user.name, user.age, user.address)  

    # .limit().offset()で途中＆取得件数絞り込み
    users = session.query(User).limit(2).offset(2).all()
    for user in users:
        print(user.id, user.name, user.age, user.address)   
    
    #列指定取得
    for user in session.query(User.id, User.name).all():
        print(user.id, user.name)
    
    #.filter()で条件指定(WHERE)
    for user in session.query(User.id, User.name).filter(User.id == 2).all(): #.allは絶対最後
        print(user.id, user.name, user.age, user.address)
    
    #AND
    for user in session.query(User.id, User.name).filter(User.name == 'a').all(): #.allは絶対最後
        print(user.id, user.name, user.age, user.address)
    
    #IN
    ids = [2, 3, 5]
    for user in session.query(User.id, User.name).filter(User.id.in_(ids)).all(): #.allは絶対最後
        print(user.id, user.name, user.age, user.address)
    


    #ORDER BY
    for user in session.query(User).order_by(User.name, User.id).all():
        print(user.id, user.name, user.age, user.address)


    #ORDER BY 2
    for user in session.query(User).order_by(desc(User.name),asc(User.id)).all:
        print(user.id, user.name, user.age, user.address)

    #.filter & order_by
    #ORDER BY
    for user in session.query(User).filter(User.name == 'a').order_by(User.name, User.id).all():
        print(user.id, user.name, user.age, user.address)

#更新
with Session(engine) as session:
   user = session.query(User).filter(User.id == 3).first()
   user.address = '千葉'
   session.commit()

#削除
with Session(engine) as session:
   user = session.query(User).filter(User.id == 4).delete()
   session.commit()