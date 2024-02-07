import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for test_case in range(1, T+1):
    result = 1
    # 2차원 배열 생성
    field = []
    for i in range(9):
        field.append(list(map(int, input().split())))
    # 가로줄 검증
    for f in field:
        temp = sorted(f)
        if test == temp:
            continue
        else:
            result = 0
            break
    # 세로줄들 가로로 만들기
    serozuls = []
    for i in range(9):
        arr = []
        for j in range(9):
            temp = field[j][i]
            arr.append(temp)
        serozuls.append(arr)
    # 세로줄 검증
    for s in serozuls:
        temp = sorted(s)
        if test == temp:
            continue
        else:
            result = 0
            break
    # 네모칸들 가로줄로 만들기
    nemos = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            ne = []
            for x in range(3):
                for y in range(3):
                    ne.append(field[i + x][j + y])
            nemos.append(ne)
    # 네모칸들 검증
    for n in nemos:
        temp = sorted(n)
        if test == temp:
            continue
        else:
            result = 0
            break
    # 테케와 함께 출력
    print(f'#{test_case} {result}')
    