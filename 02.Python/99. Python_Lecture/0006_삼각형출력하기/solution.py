import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

# 코드를 작성해주세요. 

number = int(input())

for i in range(1, number+1):
    print('*' * i)