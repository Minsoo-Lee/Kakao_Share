import google.generativeai as genai
import time, re

gemini_key = "AIzaSyC-_RsZlNX73tC--cLmz_T4c2DR0pbsMVM"
model = None

INTRO = "<br>쿠팡 활동의 일환으로 수수료를 받습니다.<br><br>"

def init_gemini():
    global model
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')


