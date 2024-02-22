import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    input_str = str(input())
    field = str(input())
    
    if input_str in field:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')