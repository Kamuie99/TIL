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
    parsed_data = response.json()
    # 사용자의 name을 dummy_data 리스트에 추가한다.
    dummy_data.append(parsed_data['name'])
    print(dummy_data)





# 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# # print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])

# # 남은 데이터 출력
# print(parsed_data['username'])
# print(parsed_data['company']['name'])