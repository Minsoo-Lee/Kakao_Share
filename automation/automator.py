import threading
from automation import driver
import wx, time
from window import log

if_login = False
is_chrome_init = False

def start_task(on_done_callback=None, on_done_login=None):
    task_thread = threading.Thread(target=set_task, args=(on_done_callback, on_done_login))
    task_thread.daemon = True  # 프로그램 종료 시 서버도 종료되도록 설정
    task_thread.start()

def set_task(on_done_callback, on_done_login):
    global if_login

    if if_login is False:
        if on_done_callback:
            wx.CallAfter(on_done_callback)  # UI 업데이트는 메인 스레드에서 안전하게 수행
        before_login(on_done_login)
        if_login = True
    # set_chrome


def before_login(on_done_login):
    global is_chrome_init

    if is_chrome_init is False:
        wx.CallAfter(log.append_log, "크롬을 초기화합니다.")
        driver.init_chrome()
        wx.CallAfter(log.append_log, "크롬 초기화 완료")
        is_chrome_init = True
    wx.CallAfter(log.append_log, "URL에 접속합니다")
    print(1)
    driver.get_url()
    print(2)
    time.sleep(1)
    print(3)
    driver.click_share_button()
    print(4)

    # 팝업창 전환 후 로그인
    driver.activate_popup()
    driver.execute_login()

    # 작업 수행 버튼 다시 활성화 하고, 로그인 인증 진행

# 로그인 했을 시 보여야 하는 요소가 뜨는지 확인
def check_login():
    pass