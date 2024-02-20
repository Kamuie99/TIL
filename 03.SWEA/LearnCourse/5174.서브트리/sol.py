import sys
sys.stdin = open('input.txt')

def counting(tree, N):
    # 현재 노드를 포함한 서브트리의 노드 개수를 저장할 변수
    count = 1
    # 현재 노드의 자식 노드들에 대해 반복
    for child_node in tree[N-1]:
        # 각 자식 노드에서 재귀적으로 서브트리의 노드 개수를 구하고 더함
        count += counting(tree, child_node)
    return count

T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    # tree로 사용할 배열 생성
    tree = [[] for _ in range(E+1)]
    # 배열로 부모 자식 노드 번호 쌍을 전달 받는다
    input_arr = list(map(int, input().split()))
    # E개의 부모 자식 노드 쌍을 하나씩 꺼내어 tree 배열에 저장
    for i in range(E):
        a = input_arr.pop(0)
        b = input_arr.pop(0)
        tree[a-1].append(b)
    # 함수를 실행한 결과를 변수에 저장하여 출력
    result = counting(tree, N)
    print(f'#{test_case} {result}')