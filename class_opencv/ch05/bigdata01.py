# 파이썬으로 REST API를 요청

import pandas
from bs4 import BeautifulSoup
import requests
from openpyxl.workbook import Workbook

apikey = "jZBvluitQuPfkA91t3EqRGJmxfxha%2Fz032GHSY0hO0Wev5Za%2FPfdPhg%2FWT%2FXSkX%2BEn4BonfsNU6WPY8e%2BDbxlQ%3D%3D"

# 약국정보서비스 API - 워드파일 다운 받아서 복붙
api = "http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList?pageNo=1&numOfRows=10&sidoCd=110000&sgguCd=110019&emdongNm=신내동&yadmNm=온누리&xPos=127.0965441345503&yPos=37.60765568913871&radius=3000&ServiceKey=[key]"

# 약국 정보 리스트
list_drugs = ["병원명", "종별코드명", "시도명", "주소", "전화번호"]
i = 0
for list_drug in list_drugs:
    url = api.format(list_drugs=list_drug, key=apikey)
    req = requests.get(url)
    re = req.text
    soup = BeautifulSoup(re, 'html.parser')

    # 병원명
    yadmnm = soup.find_all('yadmnm')

    # 종별 코드 명
    sggucdnm = soup.find_all('sggucdnm')

    # 시도명
    sidocdnm = soup.find_all('sidocdnm')

    # 주소
    addr = soup.find_all('addr')

    # 전화번호
    telno = soup.find_all('telno')

print("병원명 :", yadmnm)
print("종별 코드명: ", sggucdnm)
print("시도명 :", sidocdnm)
print("주소: ", addr)
print("전화번호: ", telno)
