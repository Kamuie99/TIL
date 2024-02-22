import sys
sys.stdin = open('input.txt')

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    
    field = [[] for _ in range(50)]
    
    for i in range(E):
        a, b = map(int, input().split())
        field[a].append(b)
        
    # 각 노드가 방문된 정보, 초기값은 다 False로 저장   
    visited = [False] * 50
    
    S, G = map(int, input().split())
    
    dfs(field, S, visited)
    
    if visited[G]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')