import urllib.request as req
from bs4 import BeautifulSoup

# 1. 서버로부터 HTML 코드 받기
code = req.urlopen("https://www.cgv.co.kr/movies/")
# print(code.read())

# 2. HTML 코드 예쁘게 정리하기
soup = BeautifulSoup(code, "html.parser")
# print(soup)

title = soup.select_one("strong.title") # tag 명이 strong, 속성명이 title 인 요소를 찾기
print(title.string)

soup.select_one("a.abc") # abc class
soup.select_one("div#movie") # id movie
soup.select_one("a > strong.title") # a의 자손
soup.select_one("div.box-contents strong.title") # div.box-contents인 요소의 후손이고, strong.title인 요소


titles = soup.select("div.sect-movie-chart strong.title")
# print(titles)
# list 자료형 하면 >>> for 문!
for i in titles:
    print(i.string) # html 요소 꺼내기
