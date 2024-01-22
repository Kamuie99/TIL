# 아래 함수를 수정하시오.
def even_elements(my_list):
    
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 != 0:
            my_list.pop(i)
        else:
            i += 1
    
    result_list = []
    result_list.extend(my_list)

    return result_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
