# 데이터베이스
# SQLite는 파이썬의 표준라이브러리로 설치가 필요없고, 선언만 하면 된다.
# 별도의 데이터베이스 애플리케이션을 사용하지 않아도 된다.
# SQLite는 웹 브라우저 내부에서 사용 가능하며, 안드로이드/iOS에서 표준으로 제공되는
# 데이터베이스이다. 가벼우면서도 표준 SQL을 사용해 데이터베이스를 처리한다.


import sqlite3


# sqlite 데이터베이스 연결하기 --- (※1)
dbpath = "test.sqlite"
# dbpath에 test.sqlite(데이터베이스 파일의 경로)를 저장한다.
conn = sqlite3.connect(dbpath)
# sqlite3.connect(dbpath)는 SQLite 데이터베이스 파일에 연결하는 함수이다.
# Connection 객체를 얻고, 데이터베이스 파일이 존재하지 않는 경우, 새롭게 파일을 생성한다.



# 테이블을 생성하고 데이터 넣기 --- (※2)
cur = conn.cursor()
# conn.cusor()는 데이터베이스를 조작하는 커서 객체를 얻는다.
# 데이터베이스에 접근하여 조작할 때 cusor()를 먼저 얻어야 한다.

cur.executescript("""
/* items 테이블이 이미 있다면 제거하기 */
DROP TABLE IF EXISTS items;

/* 테이블 생성하기 */
CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

/* items 테이블에 데이터 넣기 */
INSERT INTO items(name, price)VALUES('Apple', 800);
INSERT INTO items(name, price)VALUES('Orange', 780);  
INSERT INTO items(name, price)VALUES('Banana', 430);
""")
# executescript() 는 Python의 sqlite3 모듈에서 제공하는 메소드로,
# 여러 개의 SQL 문을 한 번에 실행할 때 사용된다.

conn.commit()
# 위의 조작을 데이터베이스에 반영한다.



# 데이터를 추출하여 출력하기 --- (※3)
cur = conn.cursor()
# 데이터베이스에 접근하여 조작할 때 cusor()를 먼저 사용해야한다.
cur.execute("SELECT item_id, name, price FROM items")
# execute()는 매개값으로 지정한 SQL문을 실행한다.
item_list = cur.fetchall()
# 실행한 결과를 모두 추출한다. 1개씩 추출하고 싶을 때는 fetchone()를 사용한다.

# 출력하기
for it in item_list:
    print(it)
    # 튜플형으로 출력된다.





















