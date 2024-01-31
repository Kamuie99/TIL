import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # 해당 케이스에서 칠할 영역개수 N을 받는다.
    N = int(input())
    # 10 * 10의 2차원 배열을 만든다.
    field = []
    for i in range(10):
        field.append([0]*10)
    # 칠할 영역 개수만큼 칸을 칠한다.
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                field[y][x] += color
    # 빨강은 1 파랑은 2 이므로 더해진 곳은 보라 3이 될 것이므로
    result = 0
    # 2차원 배열의 각 배열에서 3이 몇개인지 모두 더해 결과로 출력
    for arr in field:
        result += arr.count(3)
    # 테케와 결과를 출력
    print(f'#{test_case} {result}')