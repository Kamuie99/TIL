'''
fx = (6+5*(2-8)/2)
'''

top = -1
stack = [0] * 100

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 밖에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1} # 스택 안에서의 우선순위

fx = '(6+5*(2-8)/2)'
postfix = ''
for tk in fx:
    # 여는 괄호 push, 연산자이고 top원소보다 우선순위가 높으면 push
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
        top += 1    # push
        stack[top] = tk
    # 연산자이고 top원소보다 우선순위가 높지 않으면
    elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
        while isp[stack[top]] >= icp[tk]: # top 원소의 우선순위가 낮을 때까지 pop
            top -= 1    # pop
            postfix += stack[top+1]
        top += 1    #push
        stack[top] = tk
    elif tk == ')':     # 닫는 괄호면, 여는 괄호를 만날때까지 pop
        while stack[top] != '(':
            top -= 1    # pop
            postfix += stack[top+1]
        top -= 1    # 여는 괄호 pop 해서 버림
    else:   # 피연산자인 경우
        postfix += tk

print(postfix)