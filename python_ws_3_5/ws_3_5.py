number_of_book = 100
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address):
    increase_user()
    user_info = {'name':name, 'age':age, 'address':address}
    print(f"{name}님 환영합니다!")
    return user_info    

def decrease_book(num):
    global number_of_book
    number_of_book -= num
    return number_of_book

# rental_book 함수는 info 인자 하나만 할당 받을 수 있다.
# info 인자는 신규 고객의 이름과 나이를 담은 딕셔너리이다.
def rental_book(info):
    global number_of_book
    for key, val in info.items():
        user_name = key
        user_age = val
    num = user_age // 10
    decrease_book(num) # 신규 고객의 나이 10으로 나눈 몫 대여할 책의 수로 활용
    print(f"남은 책의 수 : {number_of_book}")
    print(f"{user_name}님이 {num}권의 책을 대여하였습니다.")

## info 인자에 사용될 딕셔너리는 many_user와 map을 사용해 새로운 딕셔너리를 생성
## 이 때, map에 사용될 함수는 lamda로 구현한다.
## 그 결과를 rental_book 함수에 각각 전달하여 호출한다.
many_user = list(map(create_user, name, age, address ))
info_list = list(map(lambda x : {x['name'] : x['age']}, many_user))
# for i in info_list:
#     rental_book(i)
list(map(rental_book, info_list))