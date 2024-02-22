import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    stops = [0] * 5001

    N = int(input())
    for i in range(N):
        start, end = map(int, input().split())
        for j in range(start, end+1):
            stops[j] += 1

    P = int(input())
    results = []
    for _ in range(P):
        temp = int(input())
        results.append(stops[temp])


    print(f'#{test_case}', *results)
