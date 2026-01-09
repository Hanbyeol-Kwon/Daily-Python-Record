# 파이썬과 MySQL 연동
# 파이썬으로 데이터베이스와 연결하면, 데이터베이스에 데이터를 입력, 수정, 조회할 수 있다.
# pymysql 라이브러리를 설치하고, MySQL과 연동하는 프로그램을 작성하는 법에 대해 알아본다.
# pymysql 라이브러리를 설치
# 명령 프롬프트에서 'pip install pymysql'을 실행한다.
# 'Successfully installed pymysql-x.x.x'와 같은 메시지가 나오면 성공이다.
# pip install은 외부 라이브러리를 설치하는 명령이다. 지금은 pymysql 라이브러리를 설치했지만,
# 필요하다면 다른 라이브러리도 동일한 방식으로 설치할 수 있다.
# 명령 프롬프트에서 exit 명령어를 실행한다.
# MySQL를 설치하고 아이디가 'dba', 비밀번호가 'dbapwd'인 사용자를 등록한 후
# 'python' 데이터베이스를 생성한다.

# import pymysql > pymysql 라이브러리 임포트
# conn = pymysql.connect() > MySQL 연결하기
# 연결자 = pymysql.connect(연결 옵션)
# 연결옵션 : host=서버IP주소, user=사용자, password=암호, db=데이터베이스, charset=문자세트
# cur = conn.cursor() > 커서 생성하기
# 커서이름 = 연결자.cursor()
# cur.execute("INSERT INTO items (name,price) VALUES ('Banana', 300)") > SQL문 수행
# 커서이름.execute("SQL문")
# 입력한 데이터 저장하기 : 연결자.commit()
# MySQL 연결 종료하기 : 연결자.close()



# pymysql 라이브러리 읽어 들이기 --- (※1)
import pymysql



# MySQL 연결하기 --- (※2)
conn = pymysql.connect(
    host='localhost',
    user='dba',
    password='dbapwd',
    db='python'
)



# 커서 추출하기 --- (※3)
cur = conn.cursor()
# conn.cusor()는 데이터베이스를 조작하는 커서 객체를 얻는다.
# 데이터베이스에 접근하여 조작할 때 cusor()를 먼저 얻어야 한다.



# 테이블 생성하기 --- (※4)
cur.execute('DROP TABLE IF EXISTS items')
# execute()는 매개값으로 지정한 SQL문을 실행한다.
cur.execute('''
    CREATE TABLE items (
        item_id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20),
        price INT
    )
''')



# 데이터 추가하기 --- (※5)
data = [('Banana', 300), ('Mango', 640), ('Kiwi', 280)]
for i in data:
    cur.execute("INSERT INTO items (name,price) VALUES (%s,%s)", i)
# SQLite에서는 SQL문 내부에 '?'로 값을 치환했는데, MySQL에서는 '%s'로 값을 치환한다.
conn.commit() # 입력한 데이터를 저장한다.



# 데이터 추출하기 --- (※6)
cur.execute("SELECT * FROM items")

for row in cur.fetchall(): # 실행한 결과를 모두 추출한다.
    print(row)
    # 튜플형으로 출력된다.
































