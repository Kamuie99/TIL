# 아래 함수를 수정하시오.
def sort_tuple(tmp):
    sorted_list = list(tmp)
    sorted_list.sort()
    new_tuple = tuple(sorted_list)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
