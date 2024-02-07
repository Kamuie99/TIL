import sys
sys.stdin = open('input.txt')
# 테스트 케이스 수
T = 10
for test_case in range(1, T+1):
    # 건물 개수
    N = int(input())
    # 배열 안에 건물 높이를 각각 저장
    field = list(map(int, input().split()))
    # 조망권 세대 수 저장할 변수 초기화
    total = 0
    # 첫번째 건물부터 마지막 건물까지
    for i in range(2, len(field)-2):
        # 건물의 왼쪽편 높이중 최고 높이
        left_side = max(field[i-2], field[i-1])
        # 건물의 오른쪽편 높이중 최고 높이
        right_side = max(field[i+2], field[i+1])
        # 만약 해당 건물의 높이가 왼쪽 오른쪽의 최고 높이보다 높다면
        if field[i] > left_side and field[i] > right_side:
            # 해당 높이와 왼쪽 오른쪽 건물의 최대 높이의 차이값을
            temp = field[i] - max(left_side, right_side)
            # 전체 조망권 세대 수 변수에 저장
            total += temp
    # 테케와 함께 조망권 세대 전체 수 출력
    print(f'#{test_case} {total}')