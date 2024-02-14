def snail(N):
    # 초기화
    snail = [[0] * N for _ in range(N)]
    num = 1
    
    # 방향 설정: 오른쪽, 아래, 왼쪽, 위 순서
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0   # 초기 방향
    
    sero, garo = 0, 0 # 초기 위치
    
    for i in range(1, N * N + 1):
        snail[sero][garo] = i
        
        # 다음 위치 계산
        next_sero, next_garo = sero + directions[d][0], garo + directions[d][1]
        
        # 범위를 벗어나거나 이미 숫자가 채워진 경우 방향을 바꿈
        if (
            next_sero < 0
            or next_sero >= N
            or next_garo < 0
            or next_garo >= N
            or snail[next_sero][next_garo] != 0
        ):
            d = (d + 1) % 4 # 방향 변경
            next_sero, next_garo = sero + directions[d][0], garo + directions[d][1]
        
        sero, garo = next_sero, next_garo
    
    return snail


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = snail(N)
    # 출력
    print(f'#{test_case}')
    for r in result:
        print(*r)