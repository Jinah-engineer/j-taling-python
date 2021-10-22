import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword)

# while True:
url = "https://www.joongang.co.kr/search/news?keyword={}".format(encoded)
code = req.urlopen(url)

soup = BeautifulSoup(code, "html.parser")
title = soup.select("h2.headline > a")

for i in title:
    print("제목 : " + i.text) # none 이라고 뜰 경우, .string 대신 .text 를 사용한다
    print("링크 : " + i.attrs["href"]) # href 의 속성값
    code_news = req.urlopen(i.attrs["href"])
    soup_news = BeautifulSoup(code_news, "html.parser")
    content = soup_news.select_one("div.article_body.fs3")
    print(content.text.strip().replace("  ", ""))
    print() # 개행

# .strip() : 문자열의 양 끝에 존재하는 공백과 \n 을 제거

'''
if len(title) == 0:
    break
for i in title:
    print(i.text)
'''

