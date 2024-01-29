import sys
sys.stdin = open('input.txt')


T = int(input())
height_arr = list(map(int, input().split()))
arr_len = len(height_arr)

result = 0
for i in range(arr_len):
    if i == 0:
        continue
    elif i != 0 and height_arr[i-1] <= height_arr[i] and height_arr[i+1] <= height_arr[i]:
        temp_arr = [height_arr[i-1], height_arr[i+1]]
        result += height_arr[i] - max(temp_arr)
