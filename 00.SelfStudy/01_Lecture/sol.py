'''


'''
def powerset(K, result, cnt):
    global count
    count += 1
    # 배열 arr에 양의 정수만 들어있고, 지속적으로 누적해 나갈 것이다.
    if cnt > 10:    # 한번이라도 누적합이 10을 넘어섰다면, 앞으로는 조사하는 의미가 없다.
        return  # 더 조사하지 말고 돌아가
    # 언제까지 조사 할 것이냐
    # K번째 원소를 사용한 경우, 사용하지 않은 경우
    if K == N:  # 모든 원소에 대해 조사를 마쳤다면.
        if cnt == 10:   # 다음 조건 : 부분 집합의 합이 10인 경우만,
            print(result)   #만들어진 부분 집합을 출력
        return
    else:   # 아직 조사해야하는 원소가 남아있는 경우
        # K번째 원소를 사용한 경우
        powerset(K+1, result + [arr[K]], cnt + arr[K])
        # K번째 원소를 사용하지 않은 경우
        powerset(K+1, result, cnt)


N = 10  # 원소의 개수가 N개
arr = list(range(1, 11))
count = 0
# 0번 요소 부터 조사, 공집합, 누적합 0
powerset(0, [], 0)
print(count)