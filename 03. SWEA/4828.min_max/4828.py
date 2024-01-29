import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    num_arr = list(map(int, input().split()))
    print(f'#{test_case} {max(num_arr) - min(num_arr)}')
    

