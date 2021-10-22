from selenium import webdriver
import time

browser = webdriver.Chrome(r"C:/projects/taling/PythonProject/chromedriver.exe")
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
time.sleep(1)

id = browser.find_element_by_css_selector("input#id")
id.send_keys("talingpython")

pw = browser.find_element_by_css_selector("input#pw")
pw.send_keys("q1w2e3!@#")

browser.find_element_by_css_selector("button#btn_login")
