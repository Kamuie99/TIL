import sys
sys.stdin = open('input.txt')
# 테스트 케이스 받기
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    temp_arr = list(map(int, input().split()))
    # 각각의 구간 합을 저장할 배열 초기화
    sum = []
    # 각 구간마다
    for i in range(0, N-M+1):
        # 구간의 합을 저장할 변수 초기화
        temp = 0
        # 해당 구간에 있는 값들을
        for j in range(i, M+i):
            # temp에 계속 저장
            temp += temp_arr[j]
        # sum 배열에 구간합 추가
        sum.append(temp)
    # sum 배열의 최대값 - 최소값 출력
    print(f'#{test_case} {max(sum) - min(sum)}')