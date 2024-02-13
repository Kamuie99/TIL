import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # N, M 값 입력 받기
    N, M = map(int, input().split())
    # 2차원 배열 다 0으로 초기화
    field = []
    for i in range(N):
        field.append([0] * N)
    
    # 중간 네 칸에 돌놔두기
    tmp = N // 2
    field[tmp-1][tmp-1] = 'W'
    field[tmp-1][tmp] = 'B'
    field[tmp][tmp-1] = 'B'
    field[tmp][tmp] = 'W'
    
    print(field)

    # 2, 3 위치에 흑돌 놓기 -> field[2][1]  # 3-1, 2-1
    # M번의 입력을 받으면서
    for j in range(M):
        y, x, dol = map(int, input().split())
        x -= 1
        y -= 1
        
        # 흑돌 놓기
        if dol == 1:
            field[x][y] = 'B'
            # 상 확인 후 교체
            nx = x - 1
            if 1 <= nx < N and field[nx][y] == 'W' and field[nx-1][y] == 'B':
                field[nx][y] = 'B'
            # 하 확인 후 교체
            nx = x + 1
            if 0 <= nx < N-1 and field[nx][y] == 'W' and field[nx+1][y] == 'B':
                field[nx][y] = 'B'
            # 좌 확인 후 교체
            ny = y - 1
            if 1 <= ny < N and field[x][ny] == 'W' and field[x][ny-1] == 'B':
                field[x][ny] = 'B'
            # 우 확인 후 교체
            ny = y + 1
            if 0 <= ny < N-1 and field[x][ny] == 'W' and field[x][ny+1] == 'B':
                field[x][ny] = 'B'
            # 좌상 확인 후 교체
            nx = x - 1
            ny = y - 1
            if 1 <= ny < N and 1 <= nx < N and field[nx][ny] == 'W' and field[nx-1][ny-1] == 'B':
                field[nx][ny] = 'B'
            # 우상 확인 후 교체
            nx = x - 1
            ny = y + 1
            if 0 <= ny < N-1 and 1 <= nx < N and field[nx][ny] == 'W' and field[nx-1][ny+1] == 'B':
                field[nx][ny] = 'B'
            # 좌하 확인 후 교체
            nx = x + 1
            ny = y - 1
            if 1 <= ny < N and 0 <= nx < N-1 and field[nx][ny] == 'W' and field[nx+1][ny-1] == 'B':
                field[nx][ny] = 'B'
            # 우하 확인 후 교체
            nx = x + 1
            ny = y + 1
            if 0 <= ny < N-1 and 0 <= nx < N-1 and field[nx][ny] == 'W' and field[nx+1][ny+1] == 'B':
                field[nx][ny] = 'B'
        # 백돌 놓기
        elif dol == 2:
            field[x][y] = 'W'
            # 상 확인 후 교체
            nx = x - 1
            if 1 <= nx < N and field[nx][y] == 'B' and field[nx-1][y] == 'W':
                field[nx][y] = 'W'
            # 하 확인 후 교체
            nx = x + 1
            if 0 <= nx < N-1 and field[nx][y] == 'B' and field[nx+1][y] == 'W':
                field[nx][y] = 'W'
            # 좌 확인 후 교체
            ny = y - 1
            if 1 <= ny < N and field[x][ny] == 'B' and field[x][ny-1] == 'W':
                field[x][ny] = 'W'
            # 우 확인 후 교체
            ny = y + 1
            if 0 <= ny < N-1 and field[x][ny] == 'B' and field[x][ny+1] == 'W':
                field[x][ny] = 'W'
            # 좌상 확인 후 교체
            nx = x - 1
            ny = y - 1
            if 1 <= ny < N and 1 <= nx < N and field[nx][ny] == 'B' and field[nx-1][ny-1] == 'W':
                field[nx][ny] = 'W'
            # 우상 확인 후 교체
            nx = x - 1
            ny = y + 1
            if 0 <= ny < N-1 and 1 <= nx < N and field[nx][ny] == 'B' and field[nx-1][ny+1] == 'W':
                field[nx][ny] = 'W'
            # 좌하 확인 후 교체
            nx = x + 1
            ny = y - 1
            if 1 <= ny < N and 0 <= nx < N-1 and field[nx][ny] == 'B' and field[nx+1][ny-1] == 'W':
                field[nx][ny] = 'W'
            # 우하 확인 후 교체
            nx = x + 1
            ny = y + 1
            if 0 <= ny < N-1 and 0 <= nx < N-1 and field[nx][ny] == 'B' and field[nx+1][ny+1] == 'W':
                field[nx][ny] = 'W'
    w_result = 0
    b_result = 0            
                
                
    for f in field:
        w_result += f.count('W')
        b_result += f.count('B')
    
    print(w_result, b_result)