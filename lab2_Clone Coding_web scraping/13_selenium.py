from selenium import webdriver
import time
browser = webdriver.Chrome("C:/Users/LG/OneDrive - 연세대학교 (Yonsei University)/문서/GitHub/DEVWOOD/lab2_Clone Coding_web scraping/chromedriver.exe")
browser.get("http://naver.com")

# browser.forward() # 앞으로 가기
# browser.back() # 뒤로 가기
# browser.refresh() # 새로 고침
#
# elem = browser.find_element_by_class_name("link_login") # 로그인 버튼
# elem.click() # 로그인 버튼 누르기
#
# elem = browser.find_element_by_id("query") # 검색창 찾기
#
# from selenium.webdriver.common.keys import Keys # 엔터 키를 누르기 위한 모듈
# elem.send_keys("검색어") # 창에 검색어 입력
# elem.send_keys(Keys.ENTER) # 엔터 누르기
#
# # tag name으로 element 찾기
# elem = browser.find_elements_by_tag_name("a")
# for e in elem:
#     e.get_attribute("href")
#
# # xpath로 element 찾기
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
#
# browser.close() # 현재 탭 닫기
# browser.quit() # 모든 탭 닫기

# 로그인 버튼 찾기
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 아이디 입력
browser.find_element_by_id("id").send_keys("naver_id")
# 비밀번호 입력
browser.find_element_by_id("pw").send_keys("naver_password")
# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)
# 아이디를 새로 입력
browser.find_element_by_id("id").clear() # 지우고
browser.find_element_by_id("id").send_keys("my_id") # 새로 입력

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
browser.quit()