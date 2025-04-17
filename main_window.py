import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials
import time, win32con, win32api, win32gui
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import time, win32con, win32api, win32gui
from apscheduler.schedulers.background import BackgroundScheduler
import re
# # 카톡창 이름, (활성화 상태의 열려있는 창)
chatroom_name = '오픈채팅방이름'


# 디데이 계산
def calculate_dday():
    today = datetime.date.today()
    test_day = datetime.date(2022,4,23)
    d_day = test_day - today
    message = "*D-day 알리미*\n정보보안기사 실기시험까지 {}일 남았습니다.".format(d_day.days)
    return message

# 채팅방에 메시지 전송
def send_text(text):

    global chatroom_name
    # 핸들_채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    send_enter(hwndEdit)


# 엔터
def send_enter(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 채팅방 열기

# 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
def open_chatroom(chatroom_name):
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx(hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx(hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx(hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx(hwndkakao_edit2_2, None, "Edit", None)

    # # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(1)   # 안정성 위해 필요
    send_enter(hwndkakao_edit3)
    time.sleep(1)


def job_1():
    global old_links, count
    open_chatroom(chatroom_name)  # 채팅방 열기
    message = calculate_dday()
    send_text(chatroom_name, message)


def main():
    global count
    sched = BackgroundScheduler()
    sched.start()
    #sched.add_job(job_1, 'cron', second='*/30', id="test_1")
    sched.add_job(job_1, 'cron', hour=9, id="test_1")
    while True:
        time.sleep(30)
        #print("Running wait")


if __name__ == '__main__':
    main()