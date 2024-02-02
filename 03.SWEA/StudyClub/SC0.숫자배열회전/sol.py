import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    field = []
    for _ in range(N):
        field.append(list(map(int, input().split())))

    # 90 도
    results_90 = []
    for i in range(N):
        temp = ''
        for j in range(N-1, -1, -1):
            temp += str(field[j][i])
        results_90.append(str(temp))

    # 180도
    results_180 = []
    for i in range(N-1, -1, -1):
        temp = ''
        for j in range(N-1, -1, -1):
            temp += str(field[i][j])
        results_180.append(str(temp))

    # 270도
    results_270 = []
    for i in range(N-1, -1, -1):
        temp = ''
        for j in range(N):
            temp += str(field[j][i])
        results_270.append(str(temp))
        
    # 출력
    print(f'#{test_case}')
    for i in range(N):
        print(f'{results_90[i]} {results_180[i]} {results_270[i]}')