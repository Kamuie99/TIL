import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    input_arr = list(map(int, input().split()))
    result = sorted(input_arr)
    print(f'#{test_case}', *result)
