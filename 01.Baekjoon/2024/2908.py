A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

result = [A, B]
print(max(result))