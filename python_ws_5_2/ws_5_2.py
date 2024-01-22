# 아래 함수를 수정하시오.
def remove_duplicates(arr):
    result1 = dict.fromkeys(arr)
    new_list = list(result1)

    return new_list


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
