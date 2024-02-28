import sys
sys.stdin = open('input.txt')

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
            