import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, data):
        # 파라미터로 받은 데이터를 삽입
        self.data = data
        # None으로 초기값을 지정 후, 노드 생성 후에 지정
        self.left = None
        self.right = None
        
class BSTree:
    def __init__ (self):
        self.root = None
        
result = Node([1,2,3,4,5,6,7,8,9])

print(list(result.root))

