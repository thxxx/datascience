import time
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()


URL = "https://play.google.com/store/movies/top"
browser.get(URL)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Accept-Language": "ko-KR,ko"}

# 지정한 위치로 스크롤 내리기
browser.execute_script("window.scrollTo(0,5080)")  # 세로 길이만큼 내린다.
# 근데 우리는 맨 밑으로 내리고 기다렸다가 내리고 해야됨

# 화면 가장 아래로 스크롤 내리고
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

interval = 3  # 2초에 한번씩 스크롤 내림
# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 우선 스크롤 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(interval)

    current_height = browser.execute_script(
        "return document.body.scrollHeight")

    if current_height == prev_height:
        break

    prev_height = current_height

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", {"class": "Vpfmgd"})
print(len(movies))

for mv in movies:
    title = mv.find("div", {"class": "WsMG1c nnK0zc"}).get_text()
    print(title)
