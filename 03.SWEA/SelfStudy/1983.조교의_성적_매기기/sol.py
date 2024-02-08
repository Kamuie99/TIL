import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    scores = dict()
    for i in range(1, N+1):
        m ,f, p = map(int, input().split())
        temp = m * 0.35 + f * 0.45 + p * 0.2
        scores[i] = round(temp, 2)
    result = sorted(scores.items(), key=lambda x : x[1], reverse=True)
    
    rank = 0
    for i in range(N):
        if result[i][0] == K:
            rank = i + 1

    tmp_1 = N // 10
    final = 0
    if rank % tmp_1 != 0:
        final += (rank // tmp_1) + 1
    else:
        final += rank // tmp_1
    
    scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    print(f'#{test_case} {scores[final-1]}')