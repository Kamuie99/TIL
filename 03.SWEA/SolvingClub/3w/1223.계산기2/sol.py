import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    field = list(input())
    stack = []
    temp = []   # 후위 표기식을 담을 arr
    
    # 후위 표기식으로 바꾸기
    for f in field:
        # 숫자이면 temp에 바로 append
        if f.isdigit():
            temp.append(f)
        # 연산자 * 이면 
        elif f == '*':
            # stack의 * 들 다 가져오기
            while stack and stack[-1] == '*':
                temp.append(stack.pop())
            stack.append(f)
        # 연산자 + 이면
        elif f == '+':
            # stack이 빌때까지 다 가져오기
            while stack:
                temp.append(stack.pop())
            stack.append(f)
    while stack:
        temp.append(stack.pop())
    
    # 후위 표기식 연산하기
    for t in temp:
        if t in '+*':
            b = stack.pop()
            a = stack.pop()
            if t == '*':
                stack.append(a * b)
            else:
                stack.append(a + b)
        else:
            stack.append(int(t))
    
    print(f'#{test_case} {stack.pop()}')
    