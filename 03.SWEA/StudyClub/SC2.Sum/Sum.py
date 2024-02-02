import sys
sys.stdin = open('input.txt')
# 테스트 케이스 10개
T = 10
for test_case in range(1, T+1):
    n = int(input())
    
    # 2차원 배열 생성
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
        
    # 가로합이 들어있는 배열
    garo_sum = []
    for i in range(100):
        garo_sum.append(sum(arr[i]))
    # 가로 합 중 최대값
    max_garo = max(garo_sum)
    
    # 세로 합이 들어있는 배열
    sero_sum = []
    for i in range(100):
        sero_temp_sum = []
        for j in range(100):
            sero_temp_sum.append(arr[j][i])
        sero_sum.append(sum(sero_temp_sum))
    # 세로 합 중 최대 값
    max_sero = max(sero_sum)
    
    # 대각선합이 들어있는 배열
    daegak_sum = []
    for i in range(100):
        daegak_sum.append(arr[i][i])
    # 대각선 합은 하나 뿐
    max_daegak = sum(daegak_sum)
    
    # 전체에서 가장 최대 값
    total_max = [max_garo, max_sero, max_daegak]
    # 결과
    result = max(total_max)
    # 테케랑 결과 출력하기
    print(f'#{test_case} {result}')