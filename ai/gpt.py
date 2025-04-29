import openai
import os
from dotenv import load_dotenv


# .env 파일에서 API 키 불러오기
# load_dotenv()
# client = openai.OpenAI(api_key=os.getenv("GPT_KEY"))

# 여기서 주석 해제 후 api_key 넣을 것
# client = openai.OpenAI(api_key="")

def get_related_url(urls):
    prompt = f"""
        이건 50개의 뉴스 링크들이야.

        {urls}

        이 중에서 '아기, 교육, 키즈 에이전시'와 관련 있는 기사 url 하나만 뽑아서 출력해 줘.
        출력은 다른 말 필요 없이 url만 건네줘.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 수많은 기사들 중 주제와 가장 적절한 기사를 뽑아내는 편집자입니다."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content
    print(content)
    return content


def get_title_body(body):
    print("=============body===========")
    print(body)
    print("============================")
    prompt = f"""
        여기 뉴스 기사가 있어.

        {body}

        이 기사를 읽고 제목을 15자가 넘지 않게, 본문은 150자 이내로 요약해 줘.
        그리고 문장 요약할 때 특수문자는 , . 이 두개만 써야 해. 다른 건 절대 쓰지 마
        물음표, 느낌표도 절대 쓰지마 제발 하지 말라는건 하지 마.
        쌍따옴표("), 홑따옴표(') 이 두개도 절대 쓰지 마
        그리고 제목과 본문 사이에 [!@#$%]라는 문자열을 넣어줘
        예시를 두 개 들어줄게.
        ================================================================================================================
        이시영, 아들과 사이판 여행 중[!@#$%]배우 이시영이 아들 정윤 군과 사이판 그로토에서 여행을 즐겼다. 스노클링 등 액티비티를 하며 추억을 쌓고, 식도락도 만끽했다. 이시영은 2017년 결혼해 2018년 아들을 출산했지만, 올해 초 이혼 절차를 밟고 있다. 드라마 꽃보다 남자, 넷플릭스 스위트홈 등 다양한 작품에 출연했다.
        ----------------------------------------------------------------------------------------------------------------
        매독, 조선을 공포로 몰아넣다[!@#$%]15세기 유럽, 콜럼버스가 아메리카 대륙에서 가져온 매독이 창궐, 1496년 이후 조선까지 전파되었다. 치료법을 몰라 사람의 간과 쓸개를 먹으면 낫는다는 미신이 퍼져, 사람 사냥과 시신 도굴이 만연했다. 선조는 포상금까지 내걸었지만, 매독은 페니실린 개발 전까지 인류를 공포에 떨게 했다. KBS 2TV 셀럽병사의 비밀에서 매독의 역사를 다룬다. 매주 화요일 오후 8시 30분 방송.
        ================================================================================================================
        처음 나오는게 제목이고, 나중에 나오는게 본문이야. 이제 잘 할 수 있지?
        """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 뉴스 기사를 주어진 조건에 맞게 일목요연하게 잘 요약하는 편집자입니다."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content
    print(content)
    result = content.split("[!@#$%]")
    print(result)
    title = result[0].strip()
    body = result[1].strip()
    print(title)
    print(body)
    return title, body
