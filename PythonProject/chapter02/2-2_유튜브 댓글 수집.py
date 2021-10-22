'''
    유튜브 댓글 수집
'''
from selenium.webdriver.chrome.options import Options

'''
    - 마우스 스크롤 동작이 필요할 때는 BeautifulSoup 모듈을 사용할 수 없다
'''

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("headless") # Chrome Headless 모드를 사용하면 브라우저 창이 켜지지 않으므로 시간 절약 가능

browser = webdriver.Chrome(r"C:/projects/taling/PythonProject/chromedriver.exe", options=option)
browser.maximize_window()
browser.get("https://www.youtube.com/watch?v=0Yj-JhVlsIA")
time.sleep(4)

# 맨 처음에 스크롤 조금 내려주기
'''
    send_keys() 함수 사용 시, 앞에 html 요소가 필요하다
'''
# 맨 처음에 스크롤 조금 내려주기
# browser.find_element_by_css_selector("html").send_keys(Keys.PAGE_DOWN)
# 맨 처음에 스크롤 끝가지 내려주기
# browser.find_element_by_css_selector("html").send_keys(Keys.END)
# time.sleep(3)

# 댓글 크롤링
comments = browser.find_elements("#content-text")
cnt = 0
for i in comments:
    print(i)

# while True:
#     try:
#         print(comments[cnt].text)
#     except Exception as e:
#         print("크롤링 끝!!")
#         print(e)
#         break
#
#     cnt += 1
#     # 댓글을 15개, 30개, 45개, 60개 출력할 때마다...
#     # 스크롤 끝까지 내려주기
#
#     if cnt % 15 == 0:
#         browser.find_element_by_css_selector("html").send_keys(Keys.END)
#         time.sleep(3)
#         comments = browser.find_elements_by_css_selector("#content-text")
#
