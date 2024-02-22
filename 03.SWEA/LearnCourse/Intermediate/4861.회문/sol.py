import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    
    arr = []
    
    for i in range(N):
        arr.append(str(input()))
    
    result = ''
    
    # 가로 탐색
    for j in range(0, len(arr)):
        for i in range(0, N-M+1):
            temp = arr[j][i:M+i]
            if temp == temp[::-1]:
                result = temp

    # 세로줄 가로로 돌리기
    serozul = []
    for i in range(0, len(arr)):
        temp = ''
        for j in range(0, len(arr)):
            temp += arr[j][i]
        serozul.append(temp)
    
    # 돌린 세로줄도 탐색
    for j in range(0, len(arr)):
        for i in range(0, N-M+1):
            temp = serozul[j][i:M+i]
            if temp == temp[::-1]:
                result = temp


    print(f'#{test_case} {result}')