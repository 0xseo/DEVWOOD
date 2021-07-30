from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window() # 전체화면으로 키워주기
url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동