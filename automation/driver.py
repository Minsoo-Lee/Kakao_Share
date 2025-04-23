import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None
URL = "https://localhost:"
PORT = "9005"
main_window = None
inp_check = None

def init_chrome():
    global driver, main_window
    if driver is None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('--start-maximized')
        # chrome_options.add_argument("--incognito")  # 시크릿 모드 추가
        driver = webdriver.Chrome(options=chrome_options)
        time.sleep(1)

    main_window = driver.current_window_handle


def get_url():
    global driver
    url = URL + PORT
    print(url)
    driver.get("http://localhost:" + PORT)
    time.sleep(1)


def click_share_button():
    # 이 부분은 UI 건들면 바뀔 수 있음
    driver.find_element(By.XPATH, "/html/body/button").click()
    time.sleep(1)

def activate_popup():
    global main_window

    # 팝업창 뜰 시간 필요
    time.sleep(1)
    all_windows = driver.window_handles

    for handle in all_windows:
        if handle != main_window:
            driver.switch_to.window(handle)
            break
    time.sleep(1)

def execute_login():
    driver.find_element(By.XPATH, "/html/body/div/div/div/main/article/div/div/form/div[1]/div/input").send_keys("minsoo1101@naver.com")
    driver.find_element(By.XPATH, "/html/body/div/div/div/main/article/div/div/form/div[2]/div/input").send_keys("msLee9164@@")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div/main/article/div/div/form/div[4]/button[1]").click()
    time.sleep(1)

def deactivate_popup():
    driver.switch_to.window(main_window)
    time.sleep(1)

def check_login():
    try:
        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div")
        return True
    except Exception as e:
        print(e)
        return False

def ready_chatroom():
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/ul/li[2]/a").click()
    time.sleep(1)

def is_chatroom_exist(room_name):
    global inp_check

    unit_chats = driver.find_elements(By.CLASS_NAME, "unit_chat")

    for chat in unit_chats:
        try:
            label = chat.find_element(By.CLASS_NAME, "tit_name")

            if label.text.strip() == room_name:
                # 해당 chat 내의 체크박스 요소 저장
                inp_check_candidate = chat.find_element(By.CLASS_NAME, "inp_check")
                inp_check = inp_check_candidate
                print("room_name = " + room_name + " / " + label.text.strip())
                return True

        except Exception as e:
            print(e)
            continue

    return False

def click_chatroom():
    global inp_check
    inp_check.click()
    time.sleep(1)

def click_share():
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/button/div/span").click()
