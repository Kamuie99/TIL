# 카운팅 정렬 연습

def counting_sorted(array):
    arr = array[:]
    max_arr = max(arr)
    count_arr = [0] * (max_arr + 1)
    
    for a in arr:
        count_arr[a] += 1
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
        
    result_arr = [0] * len(arr)
    
    for a in arr:
        result_arr[count_arr[a]-1] = a
        count_arr[a] -= 1
    
    return result_arr

A = [3, 1, 5, 9, 10, 5, 19, 2, 3, 1, 11]

print(A)

result = counting_sorted(A)

print(result)