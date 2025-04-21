from flask import Flask, render_template
import threading, os
from window import log  # log 모듈에서 가져옴


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Kakao_Share/
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')  # Kakao_Share/templates

app = Flask(__name__, template_folder=TEMPLATE_DIR)

def start_server():
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True  # 프로그램 종료 시 서버도 종료되도록 설정
    flask_thread.start()

def run_flask():
    log.append_log("서버를 시작합니다.")
    app.run(debug=True, port=8787, use_reloader=False)

@app.route('/')
def share():
    return render_template('share.html', app_key='c03ce9560aa54cba52b9fc2c4db6b3aa')