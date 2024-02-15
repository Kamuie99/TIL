import sys
sys.stdin = open('input.txt')
from collections import deque

def pw_maker(array):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque(array)
    # 0이 없음을 나타내기 위한 변수
    no_zero = True
    # 해당 큐(Queue) 안에 0이 없는 동안
    while no_zero:
        # 싸이클 실행, 1감소->2감소...->5감소
        for i in range(1, 6):
            # 큐의 제일 왼쪽에 있는 수를 가져와서
            temp = queue.popleft()
            # i 만큼 뺀 값을 temp에 할당
            temp -= i
            # 만약 temp가 0과 같거나 작아지면
            if temp <= 0:
                # temp를 0으로 유지되며
                temp = 0
                # 마지막으로 추가 후
                queue.append(temp)
                # 프로그램은 종료된다.
                no_zero = False
                break
            # temp가 0이 아니라면 계속 제일 뒤에 추가
            else:
                queue.append(temp)
    # 암호생성이 끝난 큐(Queue)를 리스트 형태로 반환
    return list(queue)
# 문제에서 그냥 입력이 10개 길래 10으로 설정
T = 10
for test_case in range(1, T+1):
    # 테스트 케이스 번호를 저장
    tc = int(input())
    # 주어지는 각 수를 integer 값으로 받아 배열로 저장
    field = list(map(int, input().split()))
    # 함수를 실행한 결과인 배열을 result 변수에 저장
    result = pw_maker(field)
    # 테케 번호와 함께 언패킹한 result 배열을 출력
    print(f'#{tc}', *result)