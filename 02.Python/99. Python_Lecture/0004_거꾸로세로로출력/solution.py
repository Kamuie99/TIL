import sys
sys.stdin = open('input.txt')

# 자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한줄씩 출력하는

number = int(input())

while number == 0:
    print(number)
    number -= 1