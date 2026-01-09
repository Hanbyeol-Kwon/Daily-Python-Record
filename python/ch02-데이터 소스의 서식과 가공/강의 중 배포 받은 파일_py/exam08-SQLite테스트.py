import sqlite3


# 데이터베이스 연결하기 --- (※1)
filepath = "test2.sqlite"
# filepath에 test2.sqlite(데이터베이스 파일의 경로)를 저장한다.
conn = sqlite3.connect(filepath)
# sqlite3.connect(filepath)는 SQLite 데이터베이스 파일에 연결하는 함수이다.
# Connection 객체를 얻고, 데이터베이스 파일이 존재하지 않는 경우, 새롭게 파일을 생성한다.



# 테이블 생성하기 --- (※2)
cur = conn.cursor()
# conn.cusor()는 데이터베이스를 조작하는 커서 객체를 얻는다.
# 데이터베이스에 접근하여 조작할 때 cusor()를 먼저 얻어야 한다.

cur.execute("DROP TABLE IF EXISTS items")
# execute()는 SQLite에 ()안에있는 SQL문을 실행한다.
cur.execute("""CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name    TEXT,
    price   INTEGER)""")
conn.commit()
# 위의 조작을 데이터베이스에 반영한다.



# 데이터 넣기 --- (※3)
cur = conn.cursor()
cur.execute("INSERT INTO items (name,price) VALUES (?,?)", ("Orange", 5200))
# SQL문에 위치홀더를 지정하고, 두번째 매개값으로 위치홀더에 치환될 값을 지정한다.
conn.commit()



# 여러 데이터 연속으로 넣기 --- (※4)
cur = conn.cursor()
data = [("Mango",7700), ("Kiwi",4000), ("Grape",8000),
        ("Peach",9400),("Persimmon",7000),("Banana", 4000)]
cur.executemany("INSERT INTO items(name,price) VALUES (?,?)", data)
# executemany()는 여러 개의 데이터를 한 번의 SQL 실행으로 처리할 수 있다.
conn.commit()



# 4000-7000원 사이의 데이터 추출하기 --- (※5)
cur = conn.cursor()
price_range = (4000, 7000)
cur.execute("SELECT * FROM items WHERE price>=? AND price<=?", price_range)
fr_list = cur.fetchall() # 실행한 결과를 모두 추출한다.

for fr in fr_list:
    print(fr)





















