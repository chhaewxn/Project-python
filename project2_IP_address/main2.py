import socket  # 컴퓨터가 연결된 접속 정보를 받아올 때 사용하는 모듈
import requests  # 사이트에 접속하기 위한 requests모듈 불러오기
import re  # IP주소를 찾기 위한 정규식을 사용하기 위한 re모듈 불러오기

# 연결된 소켓 이름을 가져와 in_addr변수와 바인딩
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))  # 구글에 접속한다. https의 기본 접속 포트는 443
print("내부 IP : ", in_addr.getsockname()[0])  # 연결된 소켓의 이름을 출력

req = requests.get("http://ipconfig.kr")  # ipconfig 사이트에 접속한다
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[
    1]  # 정규식 표현을 사용하여 IP주소를 가져와 Out_addr 변수와 바인딩
print("외부 IP: ", out_addr)  # 외부 IP주소를 출력
