import sys
sys.stdin = open('input.txt')
# 토너먼트 시작
def ko_stage(i, j):
    # 한명만 나오면 한명 우승
    if i == j:
        return i
    # 1번째 친구부터 N번째 친구까지 왼쪽 오른쪽으로 나눠서 경기진행
    else:
        left = ko_stage(i, (i+j)//2)
        right = ko_stage((i+j)//2+1, j)
        # 가위바위보 경기 진행
        return gawibawibo(left, right)
# 가위바위보 규칙
def gawibawibo(i, j):
    # 비기면 번호가 작은 쪽이 승자
    if arr[i] == arr[j]:
        return i
    # 1 가위를 냈을 때
    elif arr[i] == 1:
        if arr[j] == 2: # 상대가 바위면 j 승
            return j
        else:
            return i    # 그렇지 않으면 i 승
    # 2 바위를 냈을 때
    elif arr[i] == 2:
        if arr[j] == 3: # 상대가 보면 j 승
            return j
        else:
            return i    # 그렇지 않으면 i 승
    # 3 보를 냈을 때
    elif arr[i] == 3:
        if arr[j] == 1: # 상대가 가위면 j 승
            return j
        else:
            return i    # 그렇지 않으면 i 승

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # 앞에 0을 추가해주는 이유는 인덱스 안헷갈리려고
    arr = [0] + list(map(int, input().split()))
    print(f'#{test_case} {ko_stage(1, N)}')