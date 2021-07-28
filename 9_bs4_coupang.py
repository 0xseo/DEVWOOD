import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=" \
      "&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0" \
      "&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
hds = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
res = requests.get(url, headers=hds)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

    # 광고 제품 제외
    AD = item.find("span", attrs={"class":"ad-badge-text"})
    if AD:
        print("광고 상품")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 노트북 이름

    if "Apple" in name:
        print("애플 상품 제외")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 노트북 가격

    star = item.find("em", attrs={"class":"rating"}) # 노트북 평점

    if star: # 있으면 반환
        star = star.get_text()

    else: # 없으면 "평점 없음"
        print("평점 없음")
        continue

    reviews = item.find("span", attrs={"class":"rating-total-count"}) # 노트북 평점 수
    if reviews: # 있으면 반환
        reviews = reviews.get_text()
    else: # 없으면 "(0)"
        print("(0)")
        continue

    # 평점 5.0 이상, 평점 수 500 이상인 제품만 print
    if float(star) >= 5.0 and int(reviews[1:-1]) >= 500:
        print(name, price, star, reviews)