# 아래 함수를 수정하시오.
def get_value_from_dict(dict1, key1):
    return dict1.get(f'{key1}')


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice
