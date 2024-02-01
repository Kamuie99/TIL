import sys
sys.stdin = open('input.txt')

# 배열 길이를 구해주는 함수
def arr_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

# 내림차순 버블정렬(배열, 배열길이)
def naerim_bubblesort(array, array_len):
    # 기존의 array 배열 안건들기 위해서
    arr = array[:]
    # i는 배열의 마지막 인덱스 -> 1까지 감소
    for i in range(array_len-1, 0, -1):
        # (마지막->0) (마지막->1) ... (마지막->마지막-1) 인덱스 비교후 종료
        for j in range(array_len-1, array_len-1 - i, -1):
            # 두 값을 비교 후 오른쪽 값이 더 크면 두 값 위치 변경
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

# 선택 정렬(배열, 배열길이)
def selection_sort(array, array_len):
    # 기존의 array 배열 안건들기 위해서
    arr = array[:]
    # i는 0->(배열길이-1)까지 반복
    for i in range(array_len-1):
        # 최소값 인덱스 번호
        min_idx = i
        # i의 다음인덱스 부터 마지막까지 반복
        for j in range(i+1, array_len):
            # 만약 현재 최소값이 j인덱스 값보다 크면
            if arr[min_idx] > arr[j]:
                # j 인덱스 값이 최소값
                min_idx = j
        # 최소값 자리와 배열의 i번째 자리 값 자리 바꾸기
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

T = int(input())
for test_case in range(1, T+1):
    # 10 <= N <= 100
    N = int(input())
    # 1 <= ai <= 100 인 수들이 N개만큼
    input_arr = list(map(int, input().split()))


    # 역순으로 정렬된 sorted_arr 만들기
    # 1. 그냥 sorted() 메서드 사용하기
    # sorted_arr = sorted(input_arr, reverse=True)
    # 2. 선택 정렬 구현하기
    sorted_arr = selection_sort(input_arr, N)
    # 3. 버블 정렬 구현하기
    # sorted_arr = naerim_bubblesort(input_arr, N)


    ######## test #########
    print(input_arr)
    print(sorted_arr)
    #######################


    # 결과들을 담을 result_arr 만들기
    result_arr = []
    # 문제에서 10개까지 출력하라고 했기에 범위는 5개 * 2
    for i in range(5):
        # sorted_arr의 첫번째 수는 가장 큰 수
        result_arr.append(sorted_arr[i])
        # sorted_arr의 마지막 수는 가장 작은 수
        result_arr.append(sorted_arr[-(i+1)])
    # 결과를 담은 배열에서 공백으로 분리한 문자열로 바꾼 후 result에 저장
    result = ' '.join(str(s) for s in result_arr)


    ############ answer #############
    # print(f'#{test_case} {result}')
    #################################