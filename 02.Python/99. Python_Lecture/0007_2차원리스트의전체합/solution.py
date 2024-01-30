import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

# 코드를 작성해주세요. 

N = int(input())

total_arr = []
for i in range(1, N+1):
    arr= list(map(int, input().split()))
    total_arr.append(arr)

sum = 0
for arr in total_arr:
    for num in arr:
        sum += num

print(sum)

