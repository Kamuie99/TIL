import sys
sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    # 배열로 값을 저장받아서
    num_arr = list(map(int, input().split()))
    # 최대값 - 최소값을 출력
    print(f'#{test_case} {max(num_arr) - min(num_arr)}')