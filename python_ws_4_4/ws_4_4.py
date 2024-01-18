import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

censored_user_list = {}
def create_user(info):
    result = censorship(info['company'], info['name'])
    if result:
        info_list = []
        info_list.append(info['name'])
        censored_user_list[info['company']] = info_list
    else:
        pass
    return censored_user_list

def censorship(company_name, user_name):
    if company_name in black_list:
        print(f"{company_name} 소속의 {user_name} 은/는 등록할 수 없습니다.")
        return False
    else:
        print("이상 없습니다.")
        return True

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
    selected_info = {
            'company' : company,
            'name' : name
    }
    # 딕셔너리를 dummy_data 리스트에 삽입
    dummy_data.append(selected_info)

for i in dummy_data:
    create_user(i)

print(censored_user_list)