import requests
from bs4 import BeautifulSoup

for year in range(2016, 2021):

    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    hds = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    res = requests.get(url, headers=hds)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    imgs = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, img in enumerate(imgs):
        img_link = img["src"]
        if img_link.startswith("//"):
            img_link = "https:" + img_link

        img_res = requests.get(img_link, headers=hds) # 이미지 정보 받기
        img_res.raise_for_status()

        with open("movie{0}-{1}.jpg".format(year, idx + 1), "wb") as f:
            f.write(img_res.content) # 이미지 파일 쓰기

        if idx >= 4: # 상위 5개 영화 이미지만 다운
            break
