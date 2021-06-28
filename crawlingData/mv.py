import requests
import re
from bs4 import BeautifulSoup
import csv

URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액.csv"
# utf-8로 한글이 깨지면 utf-8-sig 하기
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
print(title)
writer.writerow(title)


for page in range(1, 2):
    res = requests.get(URL+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", {"class": "type_2"}).find(
        "tbody").find_all("tr")
    for row in data_rows:

        cols = row.find_all("td")
        if len(cols) <= 1:
            continue
        data = [col.get_text().strip() for col in cols if col != ""]
        # print(data)
        writer.writerow(data)  # 안에는 리스트 형태로 넣어줘야하기 때문에 data를 리스트로 만들었음

print("done!")
