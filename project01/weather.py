from pprint import pprint as print

import requests
import json

# 위도: 35.095776, 경도: 128.854736

city = 'Busan'
lat = 35.09
lon = 128.85
apiKey = 'bdbebd2a5dc71b08994644d806932e8e'
lang = 'kr'
units = 'metric'

# 위도 경도로 날씨 출력하기
# url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}" 

# 도시 이름으로 날씨 출력하기
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"

result = requests.get(url)
result = json.loads(result.text)

degree_k = result['main']['temp']
degree_c = degree_k - 273.15

description = result['weather'][0]['main']

print(f'{city} / {degree_c:.2f}°C / {description}')