# Flask에서 두개의 모듈을 가져왔다
from flask import Flask, request, render_template , render_template_string

# 만약 아래의 코드가 Node.js라면
# const app = new Flask(app.py); 와 같은 명령이 될 것
app = Flask(__name__)


# '@' ~에서 라는 뜻을 가지고 있는 atSign은 '데코레이터'라는 문법으로 객체지향 언어에서 매우 자주 기용하며, node.js의 Nest.js도 데코레이터를 사용한다. 
# flask 에서는  아래와 같은 방식으로 라우팅을 설정한다.
@app.route('/')
# 함수 정의가 아래가 끝이다. 중괄호를 사용하지 않기 때문에 들여쓰기가 매우 중요하다.
def index():
    return render_template('index.html')
#위의 함수는 라우팅을 통해 '/'로 들어오는 요청을 처리하는 함수로, 직관적으로 render를 위한 것이라는 것을 쉽게 알아챌 수 있다.

@app.route('/submit', methods=['POST'])

def submit():
    name = request.form['name']

    print(f'입력한 이름: {name}')


    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Submission Result</title>
        </head>
        <body>
            <h1>제출 완료!</h1>
            <p>입력하신 이름: {{ name }}</p>
            <a href="/"><button>홈으로 돌아가기</button></a>
        </body>
        </html>
    ''', name=name)
# 아래의 조건문은
# __ 언더스코어가 두개씩 들어간 코드는 일반적으로 파이썬 언어자체의 특수한 문법을 나타내는 경우가 많다.
# 파이썬 코어 
# __name__ : 현재 실행되는 스크립트
# __main__ : 메인 스크립트(엔트리 포인트)라는 뜻
# == : 비교연산자로, 자바스크립트에서는 권장하지 않는 문법이지만,
# python에서는 유일한 비교연산자이다.

# 아래의 조건문은 현재 실행되는 스크립트가 메인 스크립트인 경우에만 아래의 코드를 실행하라는 뜻
if __name__ == '__main__':
    #app이라는 변수는 위 생성한 인스턴스이고, run() 이라는 함수는 Flask 메서드이다.
     app.run(debug=True, port=5001) # debug=True는 개발자모드로 실행하라는 뜻

# 자바스크립트의 console.log()와 같은 역할을 하는 코드
# print(app)
# 자바스크립트의 console.dir()과 같은 역할을 하는 코드
# print(dir(app))