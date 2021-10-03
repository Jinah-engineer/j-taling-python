import urllib.request as req
from bs4 import BeautifulSoup
import urllib.parse as par
import os

'''
    url 주소에는 한글이 들어갈 수 없음
'''

# 이미지 저장할 폴더 만들기
if not os.path.exists("./이미지크롤링1"):
    os.mkdir("./이미지크롤링1")

keyword = input("키워드 입력 >>> ")

# 해당 키워드의 폴더 만들기
if not os.path.exists("./이미지크롤링1/{}".format(keyword)):
    os.mkdir("./이미지크롤링1/{}".format(keyword))

encoded = par.quote(keyword) # 한글 --> url 주소에 들어갈 수 있는 특수한 문자열로 변환
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(encoded)
code = req.urlopen(url)

soup = BeautifulSoup(code, "html.parser")
image = soup.select("img._image._listImage")


for i in image:
    img_url = i.attrs["data-source"] # 이미지 주소만을 추출하기
    try:
        req.urlretrieve(img_url, "./이미지크롤링1/{}/{}.png".format(keyword, image.index(i) + 1))
    except: # 위 문장에서 에러가 났다는 것은, 이미지가 존재하지 않는다는 뜻
        print("이미지 없음!")
    print("{} 이미지 크롤링 완료 {}".format("파이썬", image.index() + 1))
