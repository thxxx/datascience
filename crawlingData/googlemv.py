import time
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import collections

# browser = webdriver.Chrome("./chromedriver")
# browser.maximize_window()


URL = ["https://play.google.com/store/apps/details?id=com.intsig.camscanner",
       "https://play.google.com/store/apps/details?id=com.twitter.android",
       "https://play.google.com/store/apps/details?id=mydiary.journal.diary.diarywithlock.diaryjournal.secretdiary",
       "https://play.google.com/store/apps/details?id=com.ss.android.ugc.trill",
       "https://play.google.com/store/apps/details?id=com.komorebi.SimpleCalendar"]
# browser.get(URL)
sd = "DWdw"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Accept-Language": "ko-KR,ko"}

for i in range(5):
    result = requests.get(URL[i], headers=headers)
    result.raise_for_status()

    # soup = BeautifulSoup(browser.page_source, "lxml")
    soup = BeautifulSoup(result.text, "lxml")

    content = soup.find("div", {"jsname": "sngebd"})
    c = content.get_text()
    a = c.split(" ")
    counts = collections.Counter(a)
    if counts['수']:
        counts.pop('수')
    if counts['']:
        counts.pop('')
    if counts['할']:
        counts.pop('할')
    print(counts.most_common(10))

"""

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
"""
