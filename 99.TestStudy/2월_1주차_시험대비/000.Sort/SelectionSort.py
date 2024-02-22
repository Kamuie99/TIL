# 선택 정렬
def selection_sorted(array):
    arr = array[:]
    arr_len = len(arr)
    
    for i in range(arr_len):
        min_idx = i
        for j in range(i + 1, arr_len):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

A = [1, 9, 4, 6, 7, 2, 1, 9, 3, 4, 1, 0, 13, 11, 19, 11, 10]
result= selection_sorted(A)
print(result)