import requests
from pprint import pprint as print

# 10명의 데이터를 저장하는 리스트
dummy_data = []

for i in range(1, 11):
    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    # 필요한 정보만 가져오기
    parsed_data = response.json()
    company = parsed_data['company']['name']
    name = parsed_data['name']
    lat = float(parsed_data['address']['geo']['lat'])
    lng = float(parsed_data['address']['geo']['lng'])
    # 필요한 정보만 가져와서 새로운 딕셔너리 생성
    if -80 < lat < 80 and -80 < lng < 80:
        selected_info = {
            'company' : company,
            'lat' : lat,
            'lng' : lng,
            'name' : name
        }
    else:
        selected_info = {
            'compnay' : company,
            'name' : name
        }
    # 딕셔너리를 dummy_data 리스트에 삽입
    dummy_data.append(selected_info)


print(dummy_data)