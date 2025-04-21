import threading
from automation import driver

def start_task():
    task_thread = threading.Thread(target=execute_task)
    task_thread.daemon = True  # 프로그램 종료 시 서버도 종료되도록 설정
    task_thread.start()

def execute_task():
    driver.init_chrome()
    driver.get_url()