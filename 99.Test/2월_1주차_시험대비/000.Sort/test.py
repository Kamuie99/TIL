# 선택 정렬 오름차순

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

A = [1, 9, 4, 6, 79, 32, 56, 11, 8, 4, 2, 2, 6, 66, 27]

print(A)

result = selection_sorted(A)

print(result)

print(len(A))