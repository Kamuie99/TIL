# 배열 길이 구하는 함수
def arr_len(array):
    count = 0
    for _ in array:
        count += 1
    return count
# 오름차순 버블정렬
def oreum_bubble_sort(array, array_len):
    for i in range(array_len-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
# 내림차순 버블정렬
def naerim_bubble_sort(array, array_len):
    for i in range(array_len-1, 0, -1):
        for j in range(array_len-1, array_len-1 - i, -1):
            if array[j] > array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

# 배열이 있을 때
arr = [55, 7, 78, 12, 42]
# 해당 배열의 길이
N = arr_len(arr)
print(N)
result2 = oreum_bubble_sort(arr, N)
print(result2)
result3 = naerim_bubble_sort(arr, N)
print(result3)
