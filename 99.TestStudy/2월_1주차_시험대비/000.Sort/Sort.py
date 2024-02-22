# 버블 정렬
def bubble_sorted(array):
    arr = array[:]
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 선택 정렬
def selection_sorted(array):
    arr = array[:]
    arr_len = len(arr)
    for i in range(arr_len):
        min_idx = i
        for j in range(i+1, arr_len):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

# 카운팅 정렬
def counting_sorted(array):
    arr = array[:]
    arr_len = len(arr)
    max_arr = max(arr)
    count_arr = [0] * (max_arr + 1)
    
    for a in arr:
        count_arr[a] += 1
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    result_arr = [0] * arr_len
    
    for a in arr:
        result_arr[count_arr[a] - 1] = a
        count_arr[a] -= 1
    
    return result_arr







# 검증 부분
A = [1, 9, 4, 6, 79, 32, 56, 11, 8, 4, 2, 2, 6, 66, 27]
print(A)
result = counting_sorted(A)
print(result)