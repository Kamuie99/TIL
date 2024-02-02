# 선택 정렬

def selection_sorted(array, array_len):
    arr = array[:]
    for i in range(array_len):
        min_index = i
        for j in range(i+1, array_len):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

A = [3, 1, 5, 9, 10, 5, 19, 2, 3, 1, 11]

print(A)

result = selection_sorted(A, len(A))

print(result)