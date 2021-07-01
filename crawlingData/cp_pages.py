import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

for i in range(1, 7):
    url = f"https://www.coupang.com/np/categories/420234?channel=plp_C2&page={i}"
    # 유저 에이전트 : 진짜 사람이 직접 검색하는 것처럼.

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    # print(res)
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", {"class": re.compile("^baby-product")})
    frozen, count = 0, 0
    print("페이지 : ", i)
    for item in items:
        count += 1

        # 근데 만약 평점이 없는 상품이면?
        rating = item.find("em", {"class": "rating"})
        if rating:
            rating = rating.get_text()
        else:
            rating = "no rating"

        rtc = item.find("span", {"class": "rating-total-count"}).get_text()

        rtc = int(rtc[1:-1])
        if rtc <= 100:
            # print("리뷰가 낮아서 제외합니다.")
            continue

        # 평점이 존재하고, 평점 100개 이상인 것만 필터링 되었다.

        name = item.find("div", {"class": "name"}).get_text()
        price = item.find("strong", {"class": "price-value"}).get_text()

        # 냉동 제품 제외
        if "냉동" in name:
            frozen += 1
            # print("냉동 제품 제외합니다.")
            continue

        if float(rating) >= 4.8:
            print(f"제품명 : {name.strip()}")
            print(f"가격 : {price}")
            print(f"평점 : {rating}")
            print(f"평점 수 : {rtc}")
            print("-"*40)

    print("제외된 냉동 제품 ", frozen)
