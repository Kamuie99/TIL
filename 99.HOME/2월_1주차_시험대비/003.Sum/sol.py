import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    field = []
    for _ in range(100):
        field.append(list(map(int, input().split())))
    # 각줄의 합 담는 곳
    results = []
    # 가로 합
    for i in range(100):
        results.append(sum(field[i]))
    # 세로 합
    for i in range(100):
        hanzul = 0
        for j in range(100):
            hanzul += field[j][i]
        results.append(hanzul)
    # 대각 합 1
    temp = 0
    for i in range(100):
        temp += field[i][i]
    results.append(temp)
    # 대각 합 2
    temp = 0
    for i in range(100):
        temp += field[i][99-i]
    results.append(temp)
    # 테케와 최대값 출력
    print(f'#{test_case} {max(results)}')