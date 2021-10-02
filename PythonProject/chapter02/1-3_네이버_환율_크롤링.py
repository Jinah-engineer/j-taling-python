import urllib.request as req
from bs4 import BeautifulSoup

code = req.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(code, "html.parser")

# 1. CSS 선택자 이용해서 추출
# price = soup.select("ul#exchangeList span.value")
price = soup.select("span.value")

# 2. cnt 이용하기 (원하는 개수만큼 추출)
cnt = 0

for i in price:
    print(i.string)
    cnt += 1
    if cnt == 4:
        break


