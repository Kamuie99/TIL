import sys
sys.stdin = open('input.txt')
#전기버스 노선수
T = int(input())
for test_case in range(1, T+1):
    # K, N, M이 주어짐
    K, N, M = map(int, input().split())
    # 충전기 있는 곳 배열
    charge_arr = list(map(int, input().split()))
    # 충전기 간의 거리를 1번정류장에서 : 거리 와 같이 저장
    diff_dict = {}
    for j in range(M-1):
        diff = charge_arr[j+1] - charge_arr[j]
        diff_dict[charge_arr[j]] = diff
    diff_dict[charge_arr[-1]] = N - charge_arr[-1]
    # result 변수에 1을 할당
    result = 1
    for diff in diff_dict.values():
        # 충전기 간의 거리가 충전기 총량보다 클때는 result = 0
        if diff > K:
            result = 0
            break
        # 그렇지 않을 때는
    else:
        start = 0
        battery = K
        count = 0
        # start가 목적지 도착할 때까지, 배터리 감소 start 증가
        while start < N:
            start += 1
            battery -= 1
            # 만약 start가 정류장에 도착했고, 배터리가 다음 정류장까지 못갈 경우
            if start in charge_arr and battery < diff_dict[start]:
                # 배터리 충전
                battery = K
                # 충전 횟수 증가
                count += 1
        # 충전 횟수를 결과 값에 저장
        result = count
    # 테케와 결과 값 같이 출력      
    print(f'#{test_case} {result}')