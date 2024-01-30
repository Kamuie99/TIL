import sys
sys.stdin = open('input.txt')
# 테스트 케이스 10이라 함
T = 10
for test_case in range(1, T+1):
    # 덤프 횟수 dump
    dump = int(input())
    # 각 상자들의 높이
    heights = list(map(int, input().split()))
    # dump가 0이 될 때 까지
    while dump:
        # 최대값과 최소값 할당
        max_height = max(heights)
        min_height = min(heights)
        # 최대값 인덱스와 최소값 인덱스 가져오기
        max_index = heights.index(max_height)
        min_index = heights.index(min_height)
        # 해당 인덱스로 값 찾아가서 -1 +1
        heights[max_index] -= 1
        heights[min_index] += 1
        # 덤프 횟수 차감
        dump -= 1
    # 결과 출력
    print(f'#{test_case}', max(heights) - min(heights))