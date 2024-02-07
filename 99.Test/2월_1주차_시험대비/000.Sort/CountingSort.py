def counting_sorted(array):
    arr = array[:]
    arr_max = max(arr)
    
    count_arr = [0] * (arr_max + 1)
    
    for a in arr:
        count_arr[a] += 1
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    
    result_arr = [0] * len(arr)
    
    for a in arr:
        result_arr[count_arr[a]-1] = a
        count_arr[a] -= 1
    
    return result_arr

A = [1, 9, 4, 6, 7, 2, 1, 9, 3, 4, 1, 0, 13, 11, 19, 11, 10]
result= counting_sorted(A)
print(result)