import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome("./chromedriver")  # ./chromedriver.exe

# elem = browser.find_element_by_class_name("link_login")

# elem.click()
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_elements_by_tag_name("a")

# for e in elem:
#     e.get_attribute("href")

# elem = browser.find_element_by_xpath("//*[@id='nx_search_form']/fieldset/button")

# 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 아이디와 패스워드 입력
browser.find_element_by_id("id").send_keys("naver_id")
# browser.find_element_by_id("pw").send_keys("naver_password")
# lem = browser.find_element_by_id("log.login").click()

# 다시 입력
browser.find_element_by_id("id").clear()  # 안에 원래 있는 내용 지우기

browser.find_element_by_id("id").send_keys("zxcv05999")
browser.find_element_by_id("pw").send_keys("rlaghwls!2")
elem = browser.find_element_by_id("log.login").click()

# xpath말고 클래스, 아이디 등도 가능
try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "")))
finally:
    browser.quit()
