# 최대상금
def change(i, field):  # 최대값과 i번째 자리 수를 바꿔주는 함수
    if i >= len(field):
        return '좀만더 수정'
    # 이미 최대 값이라면 그 다음 수를 바꾸자
    if field[i] == max(field):
        return change(i+1, field)
    
    count = 0
    after_field = field[i:]
    idxes = []      # 최대값을 갖고 있는 아이들의 인덱스
    for k in range(len(after_field)):
        if after_field[k] == max(after_field):
            idxes.append(k+i)
    
    if len(idxes) == 1:
        t1 = field[i]
        t2 = field[idxes[0]]
        field[i] = t2
        field[idxes[0]] = t1

    if len(idxes) >= 2:
        t1 = field[i]
        t2 = field[idxes[-1]]
        field[i] = t2
        field[idxes[-1]] = t1
        count += 1
    
    return count

T = int(input())
for test_case in range(1, T+1):
    num, N = map(str, input().split())
    field = list(map(int, num))
    count = int(N)
    
    
    while count > 0:
        result = change(0, field)
        count -= 1
    print(field, result)
    
    
# 화물운반
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1 <= T <= 50
T = int(input())
# 다음 줄부터 테스트 케이스의 별로
for test_case in range(1, T+1):
    # 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고
    N, M = map(int, input().split())
    # 다음 줄에 N개의 화물이 무게 wi
    wi_arr = list(map(int ,input().split()))
    # 다음 줄에 M개 트럭의 적재용량 ti
    ti_arr = list(map(int, input().split()))
    # wi 배열은 내림차순으로 정렬
    wi_arr.sort(reverse = True)
    # ti 배열은 오름차순으로 정렬
    ti_arr.sort()
    # 결과를 담을 result 변수 초기화
    result = 0
    for wi in wi_arr:   # wi 배열을 순회하면서
        if ti_arr and ti_arr[-1] >= wi: # wi (가장 큰 트럭 >=현재 제일 무거운 화물)
            result += wi    # 싣어보낸 화물은 결과값에 추가
            ti_arr.pop(-1)  # 해당 트럭은 트럭 배열에서 삭제
    # 결과 값을 테케와 함께 출력
    print(f'#{test_case} {result}')
    
    
# 화물 도크
# 첫 줄에 테스트케이스의 수 T가 주어진다.
T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 첫 줄에 신청서 개수 N이 주어진다.
    field = [list(map(int, input().split())) for _ in range(N)]
    field.sort(key=lambda x: x[1])    # field 배열을 종료시간 순으로 정렬한다.
    # print(field)
    # 몇대의 화물차가 이용할 수있는지를 세줄 cnt와 종료시간을 나타낼 end
    cnt, end = 0, 0
    for i in range(N):  # 2차원 배열을 순회하면서
        s, e = field[i] # s와 e에 각각 시작시간, 종료시간 저장
        if end <= s:  # 시작시간이 직전 종료시간보다 크거나 같으면
            end = e   # 종료시간을 업데이트
            cnt += 1  # cnt +1
    print(f'#{test_case} {cnt}')