'''
0 : 현재 속도 유지
1 : 가속
2: 감속
초기 속도 0 m/s
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    result = 0
    speed = 0
    N = int(input())
    for i in range(N):
        input_arr = input()
        
        if input_arr == '0':
            result += speed
        else:
            a, b = map(int, input_arr.split())
            
            if a == 1:
                speed += b
                result += speed
            elif a == 2:
                if speed > 0:
                    speed -= b
                    result += speed
                else:
                    continue
                
    print(f'#{test_case} {result}')
    