# 카운팅 정렬

def counting_sorted(array):
    arr = array[:]
    max_int = max(arr)
    c = [0] * (max_int + 1)
    for a in arr:
        c[a] += 1
    for i in range(1, len(c)):
        c[i] += c[i-1]
    result_arr = [0] * len(arr)
    for a in arr:
        result_arr[c[a]-1] = a
        c[a] -= 1
    return result_arr

A = [3, 1, 5, 9, 10, 5, 19, 2, 3, 1, 11]

print(A)

result = counting_sorted(A)

print(result)