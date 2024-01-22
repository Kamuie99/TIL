# 아래 함수를 수정하시오.
def reverse_string(str):
    new_arr = list(str)
    new_arr.reverse()
    return_str = ''.join(new_arr)
    return return_str


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
