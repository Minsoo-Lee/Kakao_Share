from selenium.webdriver.common.by import By

from automation import driver as dr
from collections import defaultdict
from bs4 import BeautifulSoup as bs

import requests
base_url = "https://www.ibabynews.com"
url = f"{base_url}/news/articleList.html?sc_sub_section_code=S2N1&view_type=sm"

news_list = defaultdict(list)

def crawl_lists():
    global url, base_url
    response = requests.get(url)

    if response.status_code == 200:  # 정상 응답 반환 시 아래 코드블록 실행
        soup = bs(response.content, 'html.parser')  # 응답 받은 HTML 파싱
        lists = soup.find_all("div", {"class": 'list-block'})

        for l in lists:
            # 링크 추출
            a_tag = l.find("a", href=True)
            article_url = base_url + a_tag["href"]

            # 날짜 추출
            date_div = l.find("div", class_="list-dated")
            tmp_text = date_div.get_text(strip=True)
            date_text = tmp_text.split("|")[2].strip().split(" ")[0]

            # print(f"날짜: {date_text}")
            # print(f"링크: {article_url}")
            news_list[date_text].append(article_url)

            print(get_paragraph(article_url))

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
                    print(text)
                    article_text += text + "\n"  # 추출된 텍스트를 변수에 추가

        return article_text if len(article_text) > 0 else None  # 내용이 있으면 반환, 없으면 None 반환




