import sys
sys.stdin = open('input.txt')
from collections import deque

def bonaegi(arr, M):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque(arr)
    # 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 실행
    for _ in range(M):
        temp = queue.popleft()
        queue.append(temp)
    # 작업을 완료한 큐(Queue)를 리스트 형태로 반환
    return list(queue)


T = int(input())
for test_case in range(1, T+1):
    # N과 M 값을 나누어 받음
    N, M = map(int, input().split())
    # 10억 이하의 자연수들을 배열에 하나씩 저장
    field = list(map(int, input().split()))
    # 함수를 실행한 결과인 배열을 result 변수에 할당
    result = bonaegi(field, M)
    # 테스트 케이스 번호와 함께 해당 배열의 첫번째 원소를 출력
    print(f'#{test_case} {result[0]}')