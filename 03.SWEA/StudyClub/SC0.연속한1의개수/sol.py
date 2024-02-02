import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input()))

    counts = []
    count = 0
    for a in arr:
        if a == 1:
            count += 1
        else:
            if count:
                counts.append(count)
            count = 0
    counts.append(count)

    print(f'#{test_case} {max(counts)}')