import requests
from bs4 import BeautifulSoup

link = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(link)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# titles = soup.find_all("td", attrs={"class":"title"})

# title = titles[0].a.get_text()
# href = "https://comic.naver.com" + titles[0].a["href"]
# print(title)
# print(href)

# for title in titles:
#     TL = title.a.get_text()
#     href = "https://comic.naver.com" + title.a["href"]
#     print(TL, href, star)

# 평점 구하기
total = 0
titles = soup.find_all("div", attrs={"class":"rating_type"})
for title in titles:
    star = title.find("strong").get_text()
    total += float(star)
print("전체 점수 :", total)
print("평점 :", total / len(titles))