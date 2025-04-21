from selenium.webdriver.common.by import By

from automation import driver as dr
from collections import defaultdict
from bs4 import BeautifulSoup as bs
import random

import requests
BASE_URL = "https://www.ibabynews.com"
URL = f"{BASE_URL}/news/articleList.html?sc_sub_section_code=S2N1&view_type=sm"

news_list = defaultdict(list)

def crawl_lists():
    global URL, BASE_URL
    response = requests.get(URL)

    if response.status_code == 200:  # 정상 응답 반환 시 아래 코드블록 실행
        soup = bs(response.content, 'html.parser')  # 응답 받은 HTML 파싱
        lists = soup.find_all("div", {"class": 'list-block'})

        # 차라리 여기서 3개를 추출하는 것이 빠를지도
        # 아직 컨셉이 잡힌 것이 없으니 놔두자
        for l in lists:
            # 링크 추출
            a_tag = l.find("a", href=True)
            article_url = BASE_URL + a_tag["href"]

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
                    # print(text)
                    article_text += text + "\n"  # 추출된 텍스트를 변수에 추가

        return article_text if len(article_text) > 0 else None  # 내용이 있으면 반환, 없으면 None 반환

def get_random_urls():
    global news_list

    all_urls = []

    # 모든 URL을 하나의 리스트에 모으기
    for urls in news_list.values():
        all_urls.extend(urls)

    # 전체 URL 개수가 3개보다 많을 경우에만 랜덤하게 3개 선택
    if len(all_urls) >= 3:
        random_urls = random.sample(all_urls, 3)
    else:
        random_urls = all_urls  # URL 개수가 3개 미만이면 있는 만큼 모두 선택

    # 뽑아낸 3개의 URL과 내용 출력
    for i, url in enumerate(random_urls):
        print(f"--- 랜덤하게 뽑힌 URL {i + 1} ---")
        print(f"링크: {url}")
        paragraph_content = get_paragraph(url)
        if paragraph_content:
            print(f"내용:\n{paragraph_content}")
        else:
            print("내용: 해당 기사에 텍스트 내용이 없습니다.")
        print("-" * 30)



