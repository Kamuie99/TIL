T = int(input())

def time_to_min(time, minuate):
    total_min = time * 60 + minuate
    hour = total_min // 60
    min = total_min % 60
    
    if hour >= 12:
        hour -= 12
    
    return hour, min

for test_case in range(1, T+1):
    a1, b1, a2, b2 = map(int, input().split())
    hour, min = time_to_min(a1+a2, b1+b2)
    print(f'#{test_case} {hour} {min}')