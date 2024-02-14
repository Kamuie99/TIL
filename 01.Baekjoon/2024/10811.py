N, M = map(int, input().split())

field = []

for i in range(1, N+1):
    field.append(i)

for j in range(M):
    i, j = map(int, input().split())
    temp = field[i-1:j]
    temp.reverse()
    field[i-1:j] = temp

print(*field)