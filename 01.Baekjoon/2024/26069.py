N = int(input())
stack = []
for i in range(N):
    p1, p2 = map(str, input().split())
    stack.append(p1)
    stack.append(p2)
    if p1 == 'ChongChong' or p2 == 'ChongChong':
        stack = []
        stack.append(p1)
        stack.append(p2)

result1 = set(stack)
result = list(result1)
print(len(result))
        