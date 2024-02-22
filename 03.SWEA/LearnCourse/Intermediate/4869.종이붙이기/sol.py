import sys
sys.stdin = open('input.txt')

def cut(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return cut(n-1) + cut(n-2) * 2

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ans = cut(N//10)
    print(f"#{test_case} {ans}")