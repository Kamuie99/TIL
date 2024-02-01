# Counting 정렬 직접 구현해보기
def counting_sort(input_arr, max_int):
    counts = [0] * (max_int+1)

    for i in range(0, len(input_arr)):
        counts[input_arr[i]] += 1

    for i in range(1, input_arr+1):
        counts[i] += counts[i-1]

    pass



