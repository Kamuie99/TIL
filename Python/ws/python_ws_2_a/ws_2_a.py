# 아래에 코드를 작성하시오.

# zero_list 변수에 숫자 0을 하나 가지고 있는 리스트 할당
zero_list = [0]
# zero_list 변수 출력
print(zero_list)
# many_zero_list 변수에 숫자 0을 25만개 가지고 있는 리스트 할당
many_zero_list = [0]
many_zero_list *= 250000
# many_zero_list의 길이를 출력
print(len(many_zero_list))
# numbers 변수에 range를 활용하여 1부터 10까지를 가진 리스트 할당
numbers = []
numbers.extend(range(1, 11))
# numbers 변수 출력
print(numbers)
# numbers의 3번째부터 마지막 요소까지 출력한다
print(numbers[3:])