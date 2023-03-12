import requests
import re
import datetime

url = "https://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api?serviceKey=xdF4c2%2FejrJEYFVOOsmUXo4ueNyAunC75B52bGYD%2FO4%2F7GigXR8FTq5hVkarOLnLoNnFZKMS4e8ndavGalT1wA%3D%3D&pageNo=1&numOfRows=10&apiType=xml&std_day=2023-03-07"
api_key = "xdF4c2%2FejrJEYFVOOsmUXo4ueNyAunC75B52bGYD%2FO4%2F7GigXR8FTq5hVkarOLnLoNnFZKMS4e8ndavGalT1wA%3D%3D"
# 공공데이터포털에서 받은 일반 인증키 API KEY를 입력합니다.

# 오늘의 코로나19 현황을 가져오는 함수를 정의합니다. 날짜, 지역, 확진자수를 반환합니다.


def get_today_covid19(url, api_key):
    now = datetime.datetime.now()
    yyyymmdd = now.strftime('%Y%m%d')

    page_no = "&pageNo=1&numOfRows=10&"
    today = "startCreateDt=" + yyyymmdd + "&endCreateDt=" + yyyymmdd

    response = requests.get(url + api_key + page_no + today)

    gubun = re.findall(r'<gubun>(.+?)</gubun>', response.text)
    incDec = re.findall(r'<incDec>(.+?)</incDec>', response.text)

    return yyyymmdd, gubun, incDec


날짜, 지역, 확진자수 = get_today_covid19(url, api_key)
# 날짜, 지역, 확진자수의 정보를 get_today_covid19 함수를 이용하여 가져옵니다. 함수의 입력값은 url과 api키를 입력합니다.

print("날짜:", 날짜)
print("지역:", 지역)
print("확진자수:", 확진자수)
