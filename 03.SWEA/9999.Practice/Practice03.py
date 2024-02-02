import random

# 버블정렬

def bubble_sorted(array, array_len):
    arr = array[:]
    for i in range(array_len-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 선택정렬

def selection_sorted(array, array_len):
    arr = array[:]
    for i in range(array_len):
        min_idx = i
        for j in range(i+1, array_len):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

random.shuffle(A)
print(f'셔플 전: {A}')

result1 = bubble_sorted(A, len(A))
print(f'셔플 후: {result1}')

random.shuffle(A)
print(f'셔플 전: {A}')

result2 = selection_sorted(A, len(A))
print(f'셔플 후: {result1}')

