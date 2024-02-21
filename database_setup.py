import sqlite3

# 데이터베이스 연결 생성 (데이터베이스가 없으면 새로 생성)
conn = sqlite3.connect('example.db')

# 커서 객체 생성
c = conn.cursor()

# users 테이블 생성 (이미 존재한다면 먼저 삭제)
c.execute('''DROP TABLE IF EXISTS users''')
c.execute('''CREATE TABLE users (id text, password text)''')

# 사용자 추가 예제
c.execute("INSERT INTO users VALUES ('root', '1234')")
c.execute("INSERT INTO users VALUES ('chaechae', 'cherry123')")

# 변경사항 커밋
conn.commit()

# 연결 종료
conn.close()