import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
hds = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

filename = "시가총액 1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # encoding utf8은 깨져서 변경
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)


for page in range(1, 5):
    res = requests.get(url + str(page), headers=hds)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 줄바꿈 데이터 스킵
            continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)