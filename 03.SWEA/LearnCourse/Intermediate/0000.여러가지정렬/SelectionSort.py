# 선택 정렬
def selection_sort(array, array_len):
    # i는 0->(배열길이-1)까지 반복
    for i in range(array_len-1):
        # 최소값 인덱스 번호
        min_idx = i
        # i의 다음인덱스 부터 마지막까지 반복
        for j in range(i+1, array_len):
            # 만약 현재 최소값이 j인덱스 값보다 크면
            if array[min_idx] > array[j]:
                # j 인덱스 값이 최소값
                min_idx = j
        # 최소값 자리와 배열의 i번째 자리 값 자리 바꾸기
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

# 배열 길이 구하는 함수
def arr_len(array):
    count = 0
    for _ in array:
        count += 1
    return count

arr = [55, 7, 78, 12, 42]
N = arr_len(arr)
before_result = arr
print(before_result)
after_result = selection_sort(arr, N)
print(after_result)