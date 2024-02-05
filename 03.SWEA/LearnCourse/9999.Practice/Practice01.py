# 버블 정렬

def bubble_sorted(array, arr_len):
    arr = array[:]
    for i in range(arr_len-1, 0, -1):
        for j in range(0, i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

A = [3, 1, 5, 9, 10, 5, 19, 2, 3, 1, 11]

print(A)

result = bubble_sorted(A, len(A))

print(result)