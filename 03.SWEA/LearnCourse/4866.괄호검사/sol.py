import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    opened = ['(', '{']
    closed = [')', '}']
    input_s = input()
    
    gwalhos = []
    for i in input_s:
        if i in opened or i in closed:
            gwalhos.append(i)
    # print(gwalhos) # 검증 중
            
    stack = []
    result = 1
    for g in gwalhos:
        if g in opened:
            stack.append(g)
            # print(stack) # 검증 중
        else:
            if stack:
                beegyo = stack[-1]
                if closed.index(g) == opened.index(beegyo):
                    stack.pop()
                else:
                    result = 0
                    break
            else:
                result = 0
                break
    if stack:
        result = 0
    print(f'#{test_case} {result}')
            