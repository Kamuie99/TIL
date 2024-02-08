import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    input_str = str(input())
    stack = input_str[0]
    for i in range(1, len(input_str)):
        if stack == input_str[i:i+len(stack)]:
            break
        else:
            stack += input_str[i]
    print(f'#{test_case} {len(stack)}')