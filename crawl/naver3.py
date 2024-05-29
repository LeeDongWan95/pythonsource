import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = "도서검색"
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 100
ws.column_dimensions["D"].width = 20
ws.column_dimensions["E"].width = 20

# 제목 행 삽입
ws.append(["번호", "ISBN", "책제목", "가격", "할인가격"])

headers = {
    "X-Naver-Client-Id": "ufWHi_oYE6VVsv_4EZPI",
    "X-Naver-Client-Secret": "2fzgfax8Z8",
}

start, num = 1, 1
for idx in range(3):
    # idx : 0~9
    start_num = start + (idx * 100)
    url = "https://openapi.naver.com/v1/search/book.json"
    params = {"query": "베르나르 베르베르", "display": "100", "start": str(start_num)}
    r = requests.get(url, headers=headers, params=params)

    # print(r.url)

    # json 가져오기
    data = r.json()
    # print(data)
    # print(data["items"])
    for idx, item in enumerate(data["items"], 1):
        ws.append([num, item["ISBN"], item["title"], item["price"], item["discount"]])
        num += 1

base_dir = "./crawl/file/"
wb.save(base_dir + "베르나르.xlsx")
wb.close()
