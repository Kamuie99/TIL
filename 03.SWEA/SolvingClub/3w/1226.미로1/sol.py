from collections import deque
import sys
sys.stdin = open('input.txt')

def find(field, start_x, start_y):
    N = 16  # 16 * 16 행렬의 형태로 만들어진 미로
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # BFS에 사용될 큐, 시작 위치와 거리 1로 초기화
    queue = deque([(start_x, start_y)])
    # 방문한 지점 표시
    visited = [[False] * N for _ in range(N)]
    # queue에 계속해서 새로운 위치 추가, while문이 종료된다는 뜻은 가지 못했다는 뜻
    while queue:
        x, y = queue.popleft()
        # 출구 도착 확인
        if field[x][y] == 3:
            return 1
        # 네 방향 모두 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 새로운 위치가 미로 경계 내에 있는지 확인하고 아직 방문하지 않았는지 확인
            if 0 <= nx < N and 0 <= ny < N and field[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 표시
                queue.append((nx, ny))  # 큐에 새로운 위치 추가
    # 경로를 찾지 못한 경우 -1 반환
    return 0


T = 10
N = 16
for test_case in range(1, T+1):
    tc = int(input())
    # 2차원 리스트에 미로 정보 저장하기
    field = []
    for i in range(N):
        field.append(list(map(int, input())))
    # 출발점의 x 좌표, y 좌표값을 저장
    start_x = 1
    start_y = 1

    # BFS를 수행한 결과 출력
    result = find(field, start_x, start_y)
    print(f'#{test_case} {result}')