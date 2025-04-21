import threading
from automation import driver
import window.frame as frame
import ai.gemini as ai
import wx
from window import log
from automation import crawling as cr


def start_task():
    task_thread = threading.Thread(target=set_task)
    task_thread.daemon = True  # 프로그램 종료 시 서버도 종료되도록 설정
    task_thread.start()

def set_task():
    # set_chrome
    wx.CallAfter(log.append_log, "크롬을 초기화합니다.")
    driver.init_chrome()
    wx.CallAfter(log.append_log, "크롬 초기화 완료")
    wx.CallAfter(log.append_log, "URL에 접속합니다")
    driver.get_url()

    # set_gemini
    wx.CallAfter(log.append_log, "Gemini를 초기화합니다.")
    ai.init_gemini()
    wx.CallAfter(log.append_log, "Gemini를 초기화 완료")
    execute_task()

def execute_task():
    wx.CallAfter(log.append_log, "뉴스를 긁어오는 중입니다.")
    cr.crawl_lists()
