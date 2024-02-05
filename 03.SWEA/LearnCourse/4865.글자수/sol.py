import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    arr = input()
    field = input()
    
    result = {}
    
    count = 0
    for a in arr:
        temp = field.count(a)
        result[a] = temp
    
    print(f'#{test_case} {max(result.values())}')