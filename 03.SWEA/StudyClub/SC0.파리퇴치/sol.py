import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    field = []
    # field 2차원 배열 생성
    for _ in range(N):
        field.append(list(map(int, input().split())))

    result = []
    # 네모만큼 temp에 저장해서 temp를 result 배열에 append
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for x in range(M):
                for y in range(M):
                    temp += field[i + x][j + y]
            result.append(temp)
    # 테케와 함께 result 배열의 최대값 출력
    print(f'#{test_case} {max(result)}')
