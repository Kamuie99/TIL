import sys
sys.stdin = open('input.txt')
# 테스트케이스 수
T = 10
for test_case in range(1, T+1):
    # 건물의 개수 N
    N = int(input())
    # 각 건물의 높이
    heights = list(map(int, input().split()))
    # 조망권이 확보된 세대 수 초기화
    view_count = 0
    # 양쪽 끝 두 칸은 건물x 제외 후 순회
    for i in range(2, N-2):
        # 현재 건물 높이와 양쪽 두 건물의 최대 높이 차이 계산
        left_max = max(heights[i-2:i])
        right_max = max(heights[i+1:i+3])
        diff = heights[i] - max(left_max, right_max)
        # 차이가 양수면 추가
        if diff > 0:
            view_count += diff
    # 결과 출력
    print(f"#{test_case} {view_count}")