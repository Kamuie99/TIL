import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    dump = int(input())
    field = list(map(int, input().split()))
    for _ in range(dump):
        big = field.index(max(field))
        small = field.index(min(field))
        field[big] -= 1
        field[small] += 1
    result = max(field) - min(field)
    print(f'#{test_case} {result}')