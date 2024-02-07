import sys
sys.stdin = open('input.txt')

T = int(input())
# 입력 받은 값들을 2차월 배열 field에 저장
for test_case in range(1, T+1):
    y, x = map(int, input().split())
    field = []
    for _ in range(y):
        tmp = list(map(int, input().split()))
        field.append(tmp)
        
    results = []
    # 2차원 배열을 순회하면서
    for i in range(y):
        for j in range(x):
            # 값을 flower 변수에 저장
            flower = field[i][j]
            # 각 위치의 풍선가루 수를 저장할 temp 변수 초기화
            temp = 0
            # temp 변수에 자기 자신의 값 저장
            temp += flower
            # 조건을 충족하면 상하좌우의 값 temp에 저장
            for a in range(1, flower+1):
                if i-a >= 0:
                    temp += field[i-a][j]
                if i+a < y:
                    temp += field[i+a][j]
                if j-a >= 0:
                    temp += field[i][j-a]
                if j+a < x:
                    temp += field[i][j+a]
            # temp 값을 results 배열에 저장
            results.append(temp)
    # 테케와 함께 results 배열의 최대값을 출력
    print(f'#{test_case} {max(results)}')


