# 버블 정렬

def bubble_sorted(array):
    arr = array[:]
    arr_len = len(arr)
    for i in range(arr_len-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

A = [1, 9, 4, 6, 7, 2, 1, 9, 3, 4, 1, 0, 13, 11, 19, 11, 10]
result= bubble_sorted(A)
print(result)