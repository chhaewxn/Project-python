import requests
import json

city = "Seoul"  # 도시
apiKey = "29fea669e89ef7ec1c6ecc5acc315321"
lang = 'kr'  # 언어
units = 'metric'  # 화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)

print(result)

name = result['name']
lon = result['coord']['lon']
lat = result['coord']['lat']
weather = result['weather'][0]['main']
temperature = result['main']['temp']
humidity = result['main']['humidity']

print(name)
print(lon, ', ', lat)
print(weather)
print(temperature)
print(humidity)
