my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
def change_dict_set(set1, dict1):
    for item in set1:
        print(dict1.get(item))

    var = (1, 2, 3, 'A')

    dict1[var] = '변수로도 키 설정 가능'

    print(dict1)

change_dict_set(my_set, my_dict)

