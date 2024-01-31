import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    t = int(input())
    # 제일 윗줄
    field = [[0 for _ in range(102)]]
    # 다음 100줄 제일 왼쪽과 오른쪽엔 0으로 이루어진 벽
    for _ in range(100):
        temp = [0]
        arr_input = list(map(int, input().split()))
        for i in arr_input:
            temp.append(i)
        temp.append(0)
        field.append(temp)
    start_garo_index = field[100].index(2)

    garo = start_garo_index
    sero = 100
    while sero > 0:
        # 오른쪽 갈까?
        if field[sero][garo+1] == 1:
            while field[sero][garo+1] == 1:
                garo += 1
            sero -= 1
        # 왼쪽갈까?
        elif field[sero][garo-1] == 1:
            while field[sero][garo-1] == 1:
                garo -= 1
            sero -= 1
        # 올라가자
        else:
            sero -= 1

    print(garo-1)