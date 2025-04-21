import wx
from bs4 import BeautifulSoup as bs
import random
from ai import gemini
import json, threading
from window import log
from window import frame

import requests
BASE_URL = "https://www.ibabynews.com"
URL = f"{BASE_URL}/news/articleList.html?sc_sub_section_code=S2N1&view_type=sm"

news_list = []

def start_crawling():
    task_thread = threading.Thread(target=crawl_lists())
    task_thread.daemon = True  # 프로그램 종료 시 서버도 종료되도록 설정
    task_thread.start()

def crawl_lists():
    global URL, BASE_URL
    response = requests.get(URL)

    if response.status_code == 200:  # 정상 응답 반환 시 아래 코드블록 실행
        soup = bs(response.content, 'html.parser')  # 응답 받은 HTML 파싱
        lists = soup.find_all("div", {"class": 'list-block'})

        # 차라리 여기서 3개를 추출하는 것이 빠를지도
        # 아직 컨셉이 잡힌 것이 없으니 놔두자
        for i in range(3):
            print(lists[i])
            article_info = {}

            # 링크 추출
            a_tag = lists[i].find("a", href=True)
            article_url = BASE_URL + a_tag["href"]
            article_info["url"] = article_url

            # 날짜 추출
            date_div = lists[i].find("div", class_="list-dated")
            tmp_text = date_div.get_text(strip=True)
            date_text = tmp_text.split("|")[2].strip().split(" ")[0]
            article_info["date"] = date_text

            # 이미지 소스 추출
            # img_tag = lists[i].find("img", src=True)
            # print(f"img_tag: {img_tag}")
            # img_url = BASE_URL + img_tag["src"][1:]
            # print(f"img_url: {img_url}")
            # article_info["img"] = img_url

            # 제목 추출
            # 쓰레드 동기화가 걸린다면, 이건 나중에 추가하는 것도 고려해볼 만 함
            paragraph = get_paragraph(article_url)
            title = wx.CallAfter(gemini.get_response, paragraph)
            article_info["title"] = title

            response = requests.get(article_url)
            if response.status_code == 200:
                soup = bs(response.content, 'html.parser')
                lists = soup.find_all("div", {"class": 'IMGFLOATING'})

                img_tag = lists[i].find("img", src=True)
                img_url = BASE_URL + img_tag["src"]
                article_info["img"] = img_url
                print(img_url)


            # description 은 "육아"로 고정
            article_info["description"] = "육아"

            news_list.append(article_info)
    # print(json.dumps(news_list, indent=4, ensure_ascii=False))

def get_paragraph(article_url):
    response = requests.get(article_url)
    article_text = ""  # 기사 내용을 저장할 변수 초기화

    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        paragraphs = soup.find_all('p')

        for p in paragraphs:
            if p is not None:
                text = p.get_text(strip=True)
                if text is not None and len(text) > 0:
                    # print(text)
                    article_text += text + "\n"  # 추출된 텍스트를 변수에 추가

        return article_text if len(article_text) > 0 else None  # 내용이 있으면 반환, 없으면 None 반환


