import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    a, N = map(str, input().split())
    N = int(N)
    field = list(map(str, input().split()))
    
    dict = {'ZRO':0,'ONE':0,'TWO':0,'THR':0,'FOR':0,
            'FIV':0,'SIX':0,'SVN':0,'EGT':0,'NIN':0}
    
    for f in field:
        dict[f] += 1
    
    keys = list(dict.keys())
    
    print(f'#{test_case}')
    for k in keys:
        print(f'{k} ' * dict[k], end = ' ')
    print()
    