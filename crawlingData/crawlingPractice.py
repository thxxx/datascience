import requests
from bs4 import BeautifulSoup

URLs = "https://play.google.com/store/apps"
result_store = requests.get(URLs)
result_store.raise_for_status()
# store_health = requests.get("https://play.google.com/store/apps/category/HEALTH_AND_FITNESS")
print(result_store)

store_soup = BeautifulSoup(result_store.text, "lxml")
# health_soup = BeautifulSoup(store_health.text, "html.parser")

pagination = store_soup.find_all("div", {"class": "Z3lOXb"})

print(store_soup.title.get_text())
print(len(pagination))
print(pagination[0].a.get_text())

print("can i" + "do this?")
i = 0
for links in pagination:
    i += 1
    link = links.a["href"]
    print(f"link {i} is doing..")

    one_category_url = "https://play.google.com" + link

    oc_request = requests.get(one_category_url)
    oc_request.raise_for_status()

    oc_soup = BeautifulSoup(oc_request.text, "lxml")
