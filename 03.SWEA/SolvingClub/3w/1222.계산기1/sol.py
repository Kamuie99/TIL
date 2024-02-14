import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    field = list(input())
    stack = []
    result = ''
    # 후위 표기식으로 변경
    for f in field:
        if f == '+':
            while stack:
                result += stack.pop()
            stack.append(f)
        else:
            result += f
    while stack:
        result += stack.pop()
    # 스택 초기화
    stack = []
    # 후위 표기식 계산
    for r in result:
        if r == '+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(int(r))
    
    print(f'#{test_case} {stack[-1]}')