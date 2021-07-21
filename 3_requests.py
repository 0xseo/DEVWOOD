# 파이참에서 모듈 설치
# 1. File - Settings
# 2. Python Interpreter
# 3. 왼쪽 아래 + 버튼
# 4. 모듈명 검색
# 5. Install Package


import requests

nav = requests.get("http://naver.com")
goo = requests.get("http://google.com")
# nav.status_code : 링크의 정보를 제대로 받았는가 (200:정상 / 403:접근권한x)

# if nav.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("Error code", nav.status_code)

goo.raise_for_status() # 정보를 받을 수 없다면 에러를 발생시킴

print(goo.text)
with open("mygoogle.html", "w", encoding="utf8") as f: # mygoogle.html 파일에 쓰기 (utf8로)
    f.write(goo.text)