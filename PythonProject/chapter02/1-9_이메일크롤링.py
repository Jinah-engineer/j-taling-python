'''
    이메일 크롤링
'''
'''
    - BeautifulSoup 모듈에는 로그인 기능이 없다
    - selenium 모듈의 기능 : 브라우저 창을 파이썬 명령어로 제어
    
    1. pip install selenium
    2. ... > 도움말 > 크롬 정보 확인 ( = 94) 
    3. chromedriver 다운로드 
    4. chromdriver.exe - Pythonproject 폴더에 복사
'''

from selenium import webdriver
import time



option = webdriver.ChromeOptions()
option.add_argument("headless") # Chrome Headless 모드를 사용하면 브라우저 창이 켜지지 않으므로 시간 절약 가능

browser = webdriver.Chrome(r"C:/projects/taling/PythonProject/chromedriver.exe", options=option)
# 다음 로그인 사이트로 이동
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("input#id") # css 선택자로 컴퓨터에게 아이디 칸을 알려준다
# 값을 입력할 수 있는 칸의 태그명 >>> input 찾기
id.send_keys("talingpython")

pw = browser.find_element_by_css_selector("input#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("button#loginBtn").click()

# 파이썬이 너무 빠르기 때문에 실행 지연을 의도적으로 실행시켜줘야 한다
time.sleep(3)

# 이메일 함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2)

# 이메일 제목 크롤링
'''
    <beaufitulsoup>
    1. HTML 코드 서버로부터 받아오기
    2. HTML 코드 이쁘게 정리하기
    3. 원하는 요소 컴퓨터에게 알려주기 --> select(), select_one()
    
    <selenium>
    1. 원하는 요소 컴퓨터에게 알려주기 --> find_element_by_css_selector()
    
'''
title = browser.find_elements_by_css_selector("div.info_subject > a > strong.tit_subject")
for i in title:
    print(i.text) # beautifulsoup --- .string / selenium --> .text
browser.close()

'''
    셀레니움 장점
        1. 크롤링을 못하는 곳이 없다.
        2. 코드짜기 편하다.
        
    셀레니움 단점
        1. 느리다... 뷰티풀숩의 10배 정도
        2. time.sleep 의 문제가 발생한다
        
    셀레니움을 꼭 써야만 하는 상황
        1. 로그인이 필요한 사이트
        2. 웹페이지가 동적일  때, 동적 웹페이지 (ex- 유튜브 댓글 로딩)
    
    일단은 beautifulsoup 으로 시도 후, selenium 활용 
'''


