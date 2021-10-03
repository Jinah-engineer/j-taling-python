import urllib.request as req
from bs4 import BeautifulSoup

# 여러 페이지를 크롤링하고 싶다면?
'''
    1. url 주소에서 hint를 얻어야 한다.
        1, 2 페이지 비교해보기 (ex - page=1) 
'''

f = open("./알라딘중고샵.txt", 'w', encoding='utf-8')
page_num = 1

while True:
    code = req.urlopen("https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Used&KeyWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyRecentPublish=0&OutStock=0&ViewType=Detail&SortOrder=11&CustReviewCount=0&CustReviewRank=0&KeyFullWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&KeyLastWord=%ED%8C%8C%EC%9D%B4%EC%8D%AC&CategorySearch=&chkKeyTitle=&chkKeyAuthor=&chkKeyPublisher=&ViewRowCount=25&page={}"
                       .format(page_num))
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("a.bo3 > b")
    price = soup.select("a.bo_used > b")

    # for 문을 돌려야 하는 list 가 2개 있을 때는
    if len(title) == 0: # 끝 페이지까지 크롤링을 완료했다면?
        break

    for i in range(len(title)): # index 가져오기
        print(title[i].string, price[i].string)
        f.write(title[i].string + ", " + price[i].string + "\n")

    page_num += 1

f.close()
