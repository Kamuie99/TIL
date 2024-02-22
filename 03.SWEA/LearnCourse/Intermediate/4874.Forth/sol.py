import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    field = input().split()
    stack = []
    result = 'error'
    for f in field:
        # 연산자일 경우, 스택에 두개 이상 숫자가 있을 경우
        if f in '+-*/' and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            if f == '+':
                stack.append(a + b)
            elif f == '-':
                stack.append(a - b)
            elif f == '*':
                stack.append(a * b)
            elif f == '/':
                stack.append(a // b)
        # 연산자인 경우, 스택에 두개 이상 숫자가 없을 경우
        elif f in '+-*/' and len(stack) < 2:
            result = 'error'
            break
        # .이 나왔을 경우
        elif f == '.' and len(stack) == 1:
            result = stack.pop()
            break
        elif f == '.' and len(stack) > 1:
            result = 'error'
            break
        # 숫자인 경우
        else:
            stack.append(int(f))
    # 결과 출력
    print(f'#{test_case} {result}')