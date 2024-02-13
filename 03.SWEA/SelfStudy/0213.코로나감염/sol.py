from collections import deque

def corona(N, classroom):
    # 방문 여부를 저장하기 위한 2차원 배열
    visited = [[False] * N for _ in range(N)]

    # 초기 감염자의 좌표를 찾아 큐에 추가
    field = []
    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 1:
                field.append((i, j))
                visited[i][j] = True

    # 상하좌우 이동 방향
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 감염자들의 위치를 저장하는 큐
    queue = deque(field)

    days = 0
    while queue:
        # 현재 큐에 있는 모든 감염자에 대해 진행
        for _ in range(len(queue)):
            x, y = queue.popleft()

            # 상하좌우로 이동하여 감염시키기
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    # 4차 백신을 맞은 경우 감염되지 않음
                    if classroom[nx][ny] != 4:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

        # 하루가 지남
        days += 1

    return days

# 입력 받기
N = int(input())
classroom = []
for _ in range(N):
    classroom.append(list(map(int, input().split())))

# 시뮬레이션 실행
result = corona(N, classroom)
print(result)
