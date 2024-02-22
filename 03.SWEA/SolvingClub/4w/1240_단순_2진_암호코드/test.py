a = [9, 1, 5, 10, 3]


count = 0

for i in range(0, 4):
    for j in range(0, 4-i):
        if a[j] > a[j+1]:
            count += 1

print(count)