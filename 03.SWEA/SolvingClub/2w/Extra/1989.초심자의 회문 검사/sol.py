import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    test_str = str(input())
    if test_str == test_str[::-1]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')