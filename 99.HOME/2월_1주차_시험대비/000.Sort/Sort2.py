def bubble_sorted(array):
    arr = array[:]
    arr_len = len(arr)
    for i in range(arr_len-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
A = [1, 9, 4, 6, 79, 32, 56, 11, 8, 4, 2, 2, 6, 66, 27]
print(A)
result = bubble_sorted(A)
print(result)