import requests
import re

url = "https://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api?serviceKey=xdF4c2%2FejrJEYFVOOsmUXo4ueNyAunC75B52bGYD%2FO4%2F7GigXR8FTq5hVkarOLnLoNnFZKMS4e8ndavGalT1wA%3D%3D&pageNo=1&numOfRows=500&apiType=xml&std_day=2023-03-02"
response = requests.get(url)

gubun = re.findall(r'<gubun>(.+?)</gubun>', response.text)
incDec = re.findall(r'<incDec>(.+?)</incDec>', response.text)

print("지역:", gubun)
print("확진자수:", incDec)
