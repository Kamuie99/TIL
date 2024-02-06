import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    total, find = map(str, input().split())
    find_len = len(find)
    
    count = 0
    while find in total:
        total = total.replace(find, '', 1)
        count += 1
        
    result = len(total) + count
    print(f'#{test_case} {result}')