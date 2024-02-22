field = []

for i in range(28):
    n = int(input())
    field.append(n)
    
field.sort()

test = []
for i in range(1, 31):
    test.append(i)

result = []
for t in test:
    if t not in field:
        print(t)