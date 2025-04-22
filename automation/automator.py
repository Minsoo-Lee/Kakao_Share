import threading
from automation import driver
import window.frame as frame
import ai.gemini as ai
import wx
from window import log
from automation import crawling as cr


def start_task(on_done_callback=None):
    task_thread = threading.Thread(target=set_task, args=(on_done_callback,))
    task_thread.daemon = True  # 프로그램 종료 시 서버도 종료되도록 설정
    task_thread.start()

def set_task(on_done_callback):
    if on_done_callback:
        wx.CallAfter(on_done_callback)  # UI 업데이트는 메인 스레드에서 안전하게 수행
    # set_chrome
    wx.CallAfter(log.append_log, "크롬을 초기화합니다.")
    driver.init_chrome()
    wx.CallAfter(log.append_log, "크롬 초기화 완료")
    wx.CallAfter(log.append_log, "URL에 접속합니다")
    driver.get_url()


