# Counting 정렬 직접 구현해보기
def counting_sort(input_arr, max_int):
    # 정수 최대값
    m = max_int
    # 입력받은 배열
    arr = input_arr
    # count 할 배열
    c = [0] * (m+1)
    # a 등장할 때마다 c의 a 인덱스 값 + 1
    for a in arr:
        c[a] += 1
    # 이전 인덱스의 값을 더해 누적합 배열로 만든다.
    for i in range(1, m+1):
        c[i] += c[i-1]
    # 결과를 담을 배열 생성
    result = [0] * len(arr)
    # 배열의 각 요소를 인덱스로 갖는 값을 -1 한 값
    for a in arr:
        # 그 값을 인덱스로 하는 공간에 a 할당
        result[c[a]-1] = a
        # c[a] 를 -1 해준다. (안 겹치게)
        c[a] -= 1
    return result
    

