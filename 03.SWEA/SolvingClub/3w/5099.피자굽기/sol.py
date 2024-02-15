import sys
sys.stdin = open('input.txt')

from collections import deque

def fire_box(array, box_size, n_pizza):
    # 치즈양을 숫자로 저장하고 있는 피자들을 큐(Queue) 형태로 저장
    pizzas = deque(array)
    # 화덕은 이제부터 큐(Queue) 형태인 box로
    box = deque([])
    # box에 들어가는 순서(초기값 1)
    idx = 1
    # box 용량만큼 피자를 먼저 넣어요
    for i in range(box_size):
            cheeze = pizzas.popleft()
            # box에 넣을 때 순서와 치즈양을 배열 형태로 넣기
            box.append([idx, cheeze])
            # 다음 순서를 위해 + 1
            idx += 1
    # box 안에 피자가 하나만 남을때 까지 계속 뺐다 넣었다 반복
    while len(box) > 1:
        # box에서 피자 빼기
        out = box.popleft()
        # 피자는 현재 배열 형태로 1번째 인덱스 값이 치즈 양
        out[1] //= 2
        # 만약 치즈양이 0이 됐다면 
        if out[1] == 0:
            # 남은 피자가 있으면 피자를 빼서 box에 넣기
            if pizzas:
                temp = pizzas.popleft()
                box.append([idx, temp])
                idx += 1
            # 남은 피자가 없으면 그냥 빼기
            else:
                continue
        # 치즈양이 0이 아니면 다시 box에 넣고 다음 피자를 보자
        else:
            box.append(out)
    # box에 있는 마지막으로 남은 피자의 0번째 인덱스가 그 피자가 들어온 순서
    return box[0][0]


T = int(input())
for test_case in range(1, T+1):
    # 화덕의 크기 N과 피자개수 M이 주어짐
    N, M = map(int, input().split())
    # M개의 치즈양을 갖고있는 피자들을 field에 저장
    field = list(map(int, input().split()))
    # 화덕을 돌고 나온 결과를 result 변수에 저장
    result = fire_box(field, N, M)
    # 테케와 함께 result 출력
    print(f'#{test_case} {result}')