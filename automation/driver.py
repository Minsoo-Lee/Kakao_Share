import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None
URL = "http://localhost:"
PORT = "9004"
main_window = None

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

