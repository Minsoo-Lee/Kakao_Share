import threading
from automation import driver
import wx, time
from window import log

if_login = False
is_chrome_init = False

def start_task(on_done_callback=None, on_done_login=None, on_complete_login=None):
    task_thread = threading.Thread(target=set_task, args=(on_done_callback, on_done_login, on_complete_login))
    task_thread.daemon = True  # 프로그램 종료 시 서버도 종료되도록 설정
    task_thread.start()

def set_task(on_done_callback, on_done_login, on_complete_login):
    global if_login

    if if_login is False:
        if on_done_callback:
            wx.CallAfter(on_done_callback)  # UI 업데이트는 메인 스레드에서 안전하게 수행
        before_login()
        if on_done_login:
            wx.CallAfter(on_done_login)  # UI 업데이트는 메인 스레드에서 안전하게 수행
        if_login = True
        log.append_log("카카오 인증 후 작업 수행 버튼을 다시 눌러주세요.")
    else:
        if driver.check_login():
            print("SUCCESS!")
            if on_complete_login:
                wx.CallAfter(on_complete_login)
            driver.ready_chatroom()
            if driver.is_chatroom_exist("테스트"):
                driver.click_chatroom()
                driver.click_share()
                # 채팅방 닫기 구현 필요

            # 채팅 - 방 이름 탐색
            # 없으면 False 반환 - 종료
            # 있으면 계속 진행
        else:
            print("FAIL!")
            log.append_log("카카오 인증이 되지 않았습니다. 다시 시도해주세요.")


def before_login():
    global is_chrome_init

    if is_chrome_init is False:
        wx.CallAfter(log.append_log, "크롬을 초기화합니다.")
        driver.init_chrome()
        wx.CallAfter(log.append_log, "크롬 초기화 완료")
        is_chrome_init = True
    wx.CallAfter(log.append_log, "URL에 접속합니다")
    driver.get_url()
    time.sleep(1)
    driver.click_share_button()

    # 팝업창 전환 후 로그인
    driver.activate_popup()
    driver.execute_login()

    # 작업 수행 버튼 다시 활성화 하고, 로그인 인증 진행

# 로그인 했을 시 보여야 하는 요소가 뜨는지 확인

