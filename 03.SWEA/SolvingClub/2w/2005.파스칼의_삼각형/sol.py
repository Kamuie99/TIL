import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    field = []
    field.append([1])
    if N > 1:
        field.append([1, 1])
    if N > 2:
        for i in range(N-2):
            temp = []
            temp.append(1)
            before = field[i+1]
            before_len = len(field[i+1])
            for j in range(before_len-1):
                temp.append(before[j] + before[j+1])
            temp.append(1)
            field.append(temp)
    
    print(f'#{test_case}')
    for f in field:
        print(*f)