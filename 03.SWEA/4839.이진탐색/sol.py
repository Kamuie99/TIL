import sys
sys.stdin = open('input.txt')

# 이진 탐색을 몇 번 했는지 세주는 함수
def search_count(target, end):
    # 리턴할 카운트 값 초기화
    count = 0
    # 책 페이지는 모두 1에서 시작하므로 시작 값 1
    start = 1
    # 시작 페이지가 끝 페이지 보다 작거나 같을때 까지
    while start <= end:
        # 중간 페이지 값 할당
        mid = (start + end) // 2
        # 만약 중간페이지와 찾고자하는 페이지가 같으면 반복문 종료
        if mid == target:
            count += 1
            return count
        # 만약 중간페이지가 찾고자하는 페이지보다 크면 count 후 중간페이지 뒷페이지는 날리기
        elif mid > target:
            count += 1
            end = mid
        # 만약 중간페이지가 찾고자하는 페이지보다 작으면 count 후 중간페이지 앞페이지는 날리기
        else:
            count += 1
            start = mid
    # count 리턴
    return count

# 누가 이겼니 함수
def who_win(a, b):
    if a < b:
        return 'A'
    if a > b:
        return 'B'
    else:
        return 0

T = int(input())
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    # A가 탐색하는데 몇번 걸렸는지
    result_A = search_count(Pa, P)
    # B가 탐색하는데 몇번 걸렸는지
    result_B = search_count(Pb, P)
    # 누가 이겼는지 확인
    game_result = who_win(result_A, result_B)
    # 테케와 함께 출력
    print(f'#{test_case} {game_result}')
