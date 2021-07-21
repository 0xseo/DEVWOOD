import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # 가져온 html 문서를 lxml 파서를 통해 객체로 만든 것
# soup.title.get_text() : soup 객체를 통해 title 정보 얻기 (get_tilte() : 문자열만)
# soup.a : soup 객체가 가지고 있는 모든 element 정보 중에서 제일 먼저 나오는 a element 정보 반환
# soup.a.attrs) : # a가 가지고 있는 속성 dictionary 형태로 출력
# soup.a["href"]) : a의 "href" 속성 값 정보 출력
# soup.find(attrs={"class":"Nbtn_upload"}) : soup 객체에서 가장 먼저 나오는 a element 정보 중 class가 일치하는 정보 반환 // 웹툰 올리기 버튼이 하나가 아니면 태그 정보 넣어주어야 함

rank1 = soup.find("li", attrs={"class":"rank01"}) # : rank1 객체에 li 태그 안의 class 명이 rank01인 정보 저장
# print(rank1.a.get_text()) : rank1 객체 중 a 태그 정보 중에서 text만 반환

# rank2 = rank1.next_sibling.next_sibling : 다음 형제 정보 반환, 이 사이트에서는 개행정보가 있기 때문에 next_sibling을 두 번 함
# rank1 = rank2.previous_sibling.previous_sibling : 이전 형제 정보 반환
# ol = rank1.parent : 부모 정보 반환

# rank2 = rank1.find_next_sibling("li") : 다음 형제 중 제일 먼저 나오는 li 태그 정보 찾기 (개행정보 신경쓰지 않아도 됨)
# rank1.find_next_siblings("li") : 다음 형제 중 li 태그를 가진 정보 전부 반환
# webtoon = soup.find("a", text = "전지적 독자 시점-060. Ep.13 왕들의 전쟁") : 해당 text를 가진 a 태그 찾기