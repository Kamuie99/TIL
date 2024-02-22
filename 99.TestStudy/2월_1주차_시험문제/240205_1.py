# import sys
# sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    field = []
    # 과녁을 2차원 배열로 저장
    for i in range(N):
        field.append(list(map(int, input().split())))
    # 결과값들을 담을 배열
    results = []
    # 가장자리 칸은 0점이므로 가장자리가 아닌 칸들만 순회
    for i in range(1, N-1):
        for j in range(1, N-1):
            # 현재 위치 값 저장
            now = field[i][j]
            # temp에 상하좌우 값 저장
            temp = 0
            temp += field[i-1][j] + field[i+1][j] + field[i][j-1] + field[i][j+1]
            # temp - 현재 위치 값 = 보너스 점수
            result = temp - now
            # 만약 보너스 점수가 음수이면 0점
            if result < 0:
                result = 0
                results.append(result)
            # 만약 보너스 점수가 짝수이면 2배
            elif result % 2 == 0:
                result *= 2
                results.append(result)
            # 양수이면 보너스 점수로 반영
            else:
                results.append(result)
    # 보너스 점수들이 들어있는 결과 값 배열 정렬
    results.sort()
    # 가장 큰 점수는 제일 뒤에 있는 수, 테케와 함께 출력
    print(f'#{test_case} {results[-1]}')