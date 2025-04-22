from flask import Flask, render_template
import threading, os
from window import log  # log 모듈에서 가져옴
from automation import crawling as cr
import json
import wx


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Kakao_Share/
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')  # Kakao_Share/templates

app = Flask(__name__, template_folder=TEMPLATE_DIR)

def start_server(on_done_callback=None):
    flask_thread = threading.Thread(target=run_flask, args=(on_done_callback,))
    flask_thread.daemon = True  # 프로그램 종료 시 서버도 종료되도록 설정
    flask_thread.start()

def run_flask(on_done_callback):
    if on_done_callback:
        wx.CallAfter(on_done_callback)  # UI 업데이트는 메인 스레드에서 안전하게 수행

    log.append_log("서버를 시작합니다.")
    app.run(debug=True, port=8787, use_reloader=False)

@app.route('/')
def share():
    summaries = cr.news_list
    contents = []
    default_image = 'http://k.kakaocdn.net/dn/bDPMIb/btqgeoTRQvd/49BuF1gNo6UXkdbKecx600/kakaolink40_original.png'
    default_link = 'https://developers.kakao.com'

    tmp = summaries[0]
    # print(json.dumps(summaries, indent=4, ensure_ascii=False))

    for i in range(3):
        contents.append({
            'title': summaries[i]["title"],
            'description': summaries[i]["description"], # 필요에 따라 변경
            'imageUrl': summaries[i]["img"],
            'link': {
                'mobileWebUrl': summaries[i]["url"],
                'webUrl': summaries[i]["url"],
            },
        })
        print(contents[i])
        print("=" * 30)


    # summaries 리스트의 길이가 3보다 작으면 기본 contents를 채워줍니다.
    while len(contents) < 3:
        contents.append({
            'title': '기사 제목 없음',
            'description': '내용 없음',
            'imageUrl': default_image,
            'link': {
                'mobileWebUrl': default_link,
                'webUrl': default_link,
            },
        })

    return render_template('shared.html', app_key='c03ce9560aa54cba52b9fc2c4db6b3aa', contents=contents)

# @app.route('/')
# def share():
#     return render_template('share.html', app_key='c03ce9560aa54cba52b9fc2c4db6b3aa')