# 아래 함수를 수정하시오.
def count_character(str, tmp):
    count = 0
    for i in str:
        if tmp == i:
            count += 1
    return count


result = count_character("Hello, World!", "o")
print(result)  # 2
