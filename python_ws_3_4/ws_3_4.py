number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people


def create_user(name, age, address):
    increase_user()
    user_info = {'name':name, 'age':age, 'address':address}
    print(f"{name}님 환영합니다!")
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# for i in range(len(name)):
#     user_list.append(create_user(name[i], age[i], address[i]))
user_list = []

user_list = list(map(create_user, name, age, address))

print(user_list)