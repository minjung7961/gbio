from flask import Flask, render_template, request, redirect
from passlib.hash import sha256_crypt
import pymysql

app = Flask(__name__)

app.debug = True # 오류를 웹페이지 상에 보여주는 세팅 (베포할떈 False)


# 클라이언트가 http://localhost:5000/data 으로 get방식으로 요청들어왔을떄 hello world 문구를 리턴해 본다

@app.route('/', methods = ['Get']) #데코레이터 /data 는 요청들어왔을때 저경로로 중계준다는 말
def index():#이름 아무거나 해도됨
    # return "hello world"
    return render_template("index.html") # template 파일아래를 찾아 클라이언트에게 파일이 아닌 문서로 해석한다음 보낸다.
    # render_template 첫번쨰 인짜 ; 파일, 두번쨰 인자 : data 값
    # render_template 가 하는일 html 안에 파이썬문법 해석해줌 그리고 클라이언트에게 결과값을 보내줌 이능력을 엔진이라하고 그엔진명은 진자2라고 함 플라스크안에 내장되어있음

@app.route('/login', methods = ['Get','POST']) #데코레이터 /data 는 요청들어왔을때 저경로로 중계준다는 말
def login_page():#이름 아무거나 해도됨
    # return "hello world"
    return render_template("page1_login.html")    
    
@app.route('/main', methods = ['Get','POST']) #데코레이터 /data 는 요청들어왔을때 저경로로 중계준다는 말
def main_page():#이름 아무거나 해도됨
    # return "hello world"
    return render_template("main.html")   
        
# app.py 파일을 가장 먼저 실행하겠다라는 내용 (그중 이줄부터 실행할것이란 소리)
if __name__ == '__main__':
    app.run() # 애가 서버 실행시켜줌

# 서버 키려먼 이프로그램 실행하고 
# 서버 끄려면 이 프로그램 끄면 된다. -> citr + c




