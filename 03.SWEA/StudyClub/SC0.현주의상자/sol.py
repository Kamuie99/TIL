import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(1, Q+1):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            boxes[j-1] = i
    print(f'#{test_case}', *boxes)
