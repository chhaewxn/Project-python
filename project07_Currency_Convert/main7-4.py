import requests
from bs4 import BeautifulSoup


def crawling_sites(url):
    # 요청한 url을 html 문서 형식으로 받아오기
    response = requests.request('GET', url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 특정 태그의 클래스 중심으로 찾고 싶을 때는 태그 바로 뒤에 '.클래스명'을 써주고,
    # id 중심으로 찾고 싶을 때는 태그 바로 뒤에 '#id명'을 써준다
    # 아래와 같이 쓴 경우에는 'rbj0Ud' 클래스명을 가진 div의 하위 div 태그를 가리킨다.
    titles = soup.select('div.rbj0Ud div')
    places_title = []

    # titles 리스트를 돌면서 text만 places_title 리스트에 담아줌
    for one in titles:
        places_title.append(one.get_text())

    return places_title


url = 'https://www.google.com/travel/things-to-do?g2lb=4597339%2C4667459%2C4644488%2C4596364%2C4605861%2C4419364%2C4641139%2C2502548%2C2503781%2C4624411%2C4518326%2C2503771%2C4401769%2C4306835%2C4640247%2C4258168%2C4371335%2C4317915%2C4270442%2C4679298%2C4284970%2C4291517%2C4270859&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F06qd3&dest_state_type=main&dest_src=ts&q=%ED%95%9C%EA%B5%AD%20%EA%B4%80%EA%B4%91%20%EB%AA%85%EC%86%8C%20top%2010&sa=X&ved=2ahUKEwiK9Pm1hdn0AhXcr1YBHTKMBBMQuL0BegQIAxA-#ttdm=37.431297_127.251424_9&ttdmf=%252Fm%252F043pdws'
print(crawling_sites(url))
