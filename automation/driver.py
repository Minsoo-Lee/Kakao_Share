import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None
URL = "http://localhost:"
PORT = "8787"

def init_chrome():
    global driver
    if driver is None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument("--incognito")  # 시크릿 모드 추가
        driver = webdriver.Chrome(options=chrome_options)
        time.sleep(1)

def get_url():
    global driver
    url = URL + PORT
    print(url)
    driver.get("http://localhost:" + PORT)

def find_elements(by, element):
    return driver.find_elements(by, element)
