from bs4 import BeautifulSoup
import requests
import re

p = re.compile("ca.e")  # . 은 하나의 문자를 의미
# ^은 문자의 시작 : (^de) -> desk, deskfew, de 다 가능
# se$는 se로 끝나는 모든 문자 매칭


def print_match(m):
    if m:
        print("m.group()", m.group())  # 매치되면 매치된 문자, 매치안되면 에러 발생
        print("m.string()", m.string)  # 입력받은 문자
        print("m.start()", m.start())  # 입력받은 문자
        print("m.end()", m.end())  # 입력받은 문자
        print("m.span()", m.span())  # 입력받은 문자
    else:
        print("매칭 안됨")


m = p.match("case of good")  # 비교할 문자열의 처음부터 일치하는게 있는지 확인
print_match(m)

n = p.search("goot case")  # 비교할 문자열 중에 일치하는게 있는지 확인
print_match(n)

lst = p.findall("good case cafe")
print(lst)
