import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    M = int(input())
    N = 8
    field = []
    # 배열에 문자열로 다 넣기
    for i in range(N):
        field.append(str(input()))
    # 가로 탐색
    count = 0
    for i in range(0, N):
        for j in range(0, N-M+1):
            temp = field[i][j:M+j]
            if temp == temp[::-1]:
                count += 1
    # 세로줄 가로로 돌리기
    garozulro = []
    for i in range(N):
        temp = ''
        for j in range(N):
            temp += field[j][i]
        garozulro.append(temp)
    # 세로줄 탐색
    for i in range(0, N):
        for j in range(0, N-M+1):
            temp = garozulro[i][j:M+j]
            if temp == temp[::-1]:
                count += 1
    # 테케와 함께 출력
    print(f'#{test_case} {count}')