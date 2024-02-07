import sys
sys.stdin = open('input.txt')

def zarugi(string):
    input_s = string
    N = len(input_s)
    stack = []
    for i in range(N):
        if stack:
            if stack[-1] == input_s[i]:
                return zarugi(input_s[:i-1] + input_s[i+1:])
            else:
                stack.append(input_s[i])
        else:
            stack.append(input_s[i])
    return input_s

T = 10
for test_case in range(1, T+1):
    N, what = map(str, input().split())
    N = int(N)
    print(f'#{test_case} {zarugi(what)}')
    