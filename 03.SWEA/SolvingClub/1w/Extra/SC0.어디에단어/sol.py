import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    field = []
    for _ in range(N):
        field.append(list(map(int, input().split())))

    # 가로줄 확인
    garo_results = []
    for i in range(N):
        count = 0
        for j in range(N):
            if field[i][j] == 1:
                count += 1
                if j == N-1:
                    garo_results.append(count)
            else:
                if count:
                    garo_results.append(count)
                    count = 0
    garo_result = garo_results.count(K)

    # 세로줄 확인
    sero_results = []
    for i in range(N):
        count = 0
        for j in range(N):
            if field[j][i] == 1:
                count += 1
                if j == N-1:
                    sero_results.append(count)
            else:
                if count:
                    sero_results.append(count)
                    count = 0
    sero_result = sero_results.count(K)

    total_result = garo_result + sero_result
    print(f'#{test_case} {total_result}')
