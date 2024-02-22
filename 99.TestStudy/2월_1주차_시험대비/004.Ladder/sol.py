import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    n = int(input())
    
    # 2차원 배열 field 만들기
    field = []
    temp = []
    # 첫 줄에 0이 102개 들어있는 한 줄
    for _ in range(102):
        temp.append(0)
    field.append(temp)
    # 다음 100줄은 양 끝이 0인 input_arr을 field에 추가
    for _ in range(100):
        tmp = [0]
        arr_input = (list(map(int, input().split())))
        for a in arr_input:
            tmp.append(a)
        tmp.append(0)
        field.append(tmp)
    # x축 시작값 찾기
    start_x = field[100].index(2)
    start_y = 100
    # 현재 x,y 인덱스 저장
    x = start_x
    y = start_y
    
    while y > 0:
        # 오른쪽?
        if field[y][x+1] == 1:
            while field[y][x+1] == 1:
                x += 1
            y -= 1
        # 왼쪽?
        elif field[y][x-1] == 1:
            while field[y][x-1] == 1:
                x -= 1
            y -= 1
        else:
            y -= 1
        
    print(f'#{test_case} {x-1}')