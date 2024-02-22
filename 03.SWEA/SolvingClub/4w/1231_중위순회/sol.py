import sys
sys.stdin = open('input.txt')

def in_order_traversal(node, tree):
    # 재귀적으로 왼쪽 자식 노드를 순회
    if node != 0:
        in_order_traversal(tree[node][1], tree)
        # 현재 노드의 문자를 결과 리스트에 추가
        result.append(tree[node][0])
        # 재귀적으로 오른쪽 자식 노드를 순회
        in_order_traversal(tree[node][2], tree)

def find_word(test_case, tree):
    global result
    result = []
    # 루트 노드부터 in-order 순회 시작
    in_order_traversal(1, tree)
    # 리스트에 저장된 문자들을 결합하여 단어 생성
    word = ''.join(result)
    # 출력 형식에 맞게 결과 출력
    print(f"#{test_case} {word}")

# 테스트 케이스 수
T = 10
for test_case in range(1, T + 1):
    # 정점의 총 수 입력
    N = int(input())
    # 트리 구성
    tree = {}
    for _ in range(N):
        data = input().split()
        node = int(data[0])
        left_child = int(data[2]) if len(data) > 2 else 0
        right_child = int(data[3]) if len(data) > 3 else 0
        tree[node] = (data[1], left_child, right_child)
    # 단어 찾기 및 출력
    find_word(test_case, tree)

