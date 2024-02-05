import sys
sys.stdin = open('input.txt')
# 테스트 케이스를 입력 받는다.
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    temp = str(input())
    temp_arr = []
    # 해당 문자열을 배열로 받는다.
    for i in range(0, len(temp)):
        temp_arr.append(temp[i])
    # 배열과 set를 준비한다.
    temp_set = set(temp_arr)
    # 빈 딕셔너리를 초기화
    temp_dict = {}
    for check in temp_set:
        # 세트를 순회하며 해당 값을 배열에서 count 하여 딕셔너리에
        count = temp_arr.count(check)
        # 해당값:등장횟수로 저장한다.
        temp_dict[f'{check}'] = count
    # 딕셔너리에서 제일 큰 value를 갖는 key값들을 max_arr 배열에 저장한다.
    max_arr = [k for k,v in temp_dict.items() if max(temp_dict.values()) == v]
    # max_arr 배열에서 가장 큰 값이 결과 값이다.
    result = max(max_arr)
    # 해당 값의 value를 가져온다.
    value = temp_dict[f'{result}']
    # 두가지를 테케 번호와 같이 출력한다.
    print(f'#{test_case} {result} {value}')