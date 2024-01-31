import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # 각 테케 첫 번째 줄에 N이 주어짐
    N = int(input())
    # 나머지를 담을 배열 생성
    rem_arr = [0] * 5
    # N이 1 보다 큰 경우 계속 나누기
    while N > 1:
        # 11로 나눈 몫은 다시 계산, 나머지는 저장
        if N % 11 == 0:
            N //= 11
            rem_arr[4] += 1
        elif N % 7 == 0:
            N //= 7
            rem_arr[3] += 1
        elif N % 5 == 0:
            N //= 5
            rem_arr[2] += 1
        elif N % 3 == 0:
            N //= 3
            rem_arr[1] += 1
        elif N % 2 == 0:
            N //= 2
            rem_arr[0] += 1
    # 나머지들이 담겨있는 배열을 .join을 사용하여 문자열 변환 후 result 변수에 저장
    result = ' '.join(str(s) for s in rem_arr)
    # 테케번호와 같이 결과 출력
    print(f'#{test_case} {result}')
