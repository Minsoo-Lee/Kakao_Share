import google.generativeai as genai
import time, re

gemini_key = "AIzaSyA1eJ6rzCHxHzrLoLb7OvjamMjmo9XzdY8"
model = None

def init_gemini():
    global model
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')


def get_response(p, max_retries=5):
    """
    Fetch a response using the Gemini API with retry logic
    implemented to handle rate limits (429 errors).
    """
    global model

    # Request to the Gemini API
    response = model.generate_content(
        f"""
        이건 내가 스크랩한 기사야. 다음 기사를 제목으로 쓸 수 있도록 15자가 넘지 않게 간결하게 요약해 줘

        {p}
        """
    )
    print("[response] = " + response.text)
    return response.text



# def get_response(p):
#     global model
#     response = None
#     while response is None:
#         response = model.generate_content(f"""
#                     이건 내가 스크랩한 기사야. 다음 기사를 제목으로 쓸 수 있도록 15자가 넘지 않게 간결하게 요약해 줘
#
#                     {p}""")
#
#     return response.text


