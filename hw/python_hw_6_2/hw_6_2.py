# 아래 함수를 수정하시오.
def remove_duplicates_to_set(item):
    tmp = set(item)
    return list(tmp)


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
