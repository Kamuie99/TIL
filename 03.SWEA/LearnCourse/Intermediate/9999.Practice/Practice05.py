# 카운팅 정렬 연습

def counting_sorted(array, max_int):
    arr = array
    m = max_int
    c = [0] * (m+1)
    for a in arr:
        c[a] += 1
    for i in range(1, m+1):
        c[i] += c[i-1]
    result_arr = [0] * len(arr)
    for a in arr:
        result_arr[c[a]-1] = a
        c[a] -= 1
    return result_arr

A = [3, 1, 5, 9, 10, 5, 19, 2, 3, 1, 11]

print(A)

result = counting_sorted(A, max(A))

print(result)