import requests
from bs4 import BeautifulSoup
import re

one_category_url = "https://play.google.com/store/apps/collection/cluster?clp=ogooCAEaHAoWcmVjc190b3BpY19jZ1lCeGhIdmk2cxA7GAMqAggBUgIIAg%3D%3D:S:ANO1ljJyQ-M&gsr=CiuiCigIARocChZyZWNzX3RvcGljX2NnWUJ4aEh2aTZzEDsYAyoCCAFSAggC:S:ANO1ljJ4RbA"

oc_request = requests.get(one_category_url)
oc_request.raise_for_status()

oc_soup = BeautifulSoup(oc_request.text, "lxml")

another_a = oc_soup.find_all("a", {"class": "poRVub"})

# for one_app in another_a:
#     one_link = one_app["href"]


for one_app in range(4):
    print(f"{one_app} number is progressing..")
    one_link = another_a[one_app]["href"]
    # 여기까지가 체인지
    one_url = "https://play.google.com" + one_link

    oa_request = requests.get(one_url)
    oa_request.raise_for_status()

    oa_soup = BeautifulSoup(oa_request.text, "lxml")
    oa_title = oa_soup.find("div", {"class": "sIskre"}).find(
        "h1", {"class": "AHFaub"})
    oa_download_numbers = oa_soup.find("span", {"class", "AYi5wd TBRnV"})
    oa_rating = oa_soup.find("div", {"class": "BHMmbe"})
    oa_infos = oa_soup.find_all("div", {"class": "hAyfc"})
    oa_infos_title = oa_soup.find_all("div", {"class": "BgcNfc"})

    print("앱 이름 : ", oa_title.span.get_text())
    print("리뷰 수 : ", oa_download_numbers.span.get_text())
    print("별점 : ", oa_rating.get_text())
    print(oa_infos_title[0].get_text(), oa_infos[0].find(
        "span", {"class": "htlgb"}).get_text())
    print(oa_infos_title[1].get_text(), oa_infos[1].find(
        "span", {"class": "htlgb"}).get_text())
    print(oa_infos_title[2].get_text(), oa_infos[2].find(
        "span", {"class": "htlgb"}).get_text())

    print("")
