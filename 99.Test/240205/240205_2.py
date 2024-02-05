# import sys
# sys.stdin = open('algo2_sample_in.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    field = list(map(int, input().split()))
    # 현재 인덱스
    idx = 0
    # 누적합 변수
    result = 0
    # 마지막 음수 점프
    l_jump = 0
    while K > 0:
        # 처음부터 음수면 끝
        if field[0] < 0:
            break
        # 처음부터 양수일 때만 시작
        else:
            # 양수이면 앞으로 가기
            if field[idx] > 0:
                # 가야될 칸 수 = 현재 수 + 직전 음수 점프 수
                go = field[idx] + l_jump
                # 음수 점프 했으니 0
                l_jump = 0
                # 다음 idx 는 현재 가야될 칸수만큼 간 곳
                idx += go
                # 만약 idx가 범위를 벗어나지 않았다면
                if 0 <= idx < len(field):
                    result += field[idx]  # 결과 값에 반영
                # 범위를 벗어났으면 종료
                else:
                    break
                # 점프 수 1회 감소
                K -= 1
            # 음수이면 뒤로 가기
            elif field[idx] < 0:
                # 가야될 칸 수 = 현재 수만큼 음수니 뒤로 감
                go = field[idx]
                # 다음 idx 는 현재 가야될 칸수만큼 간 곳
                idx += go
                # 다음 양수가 되면 추가로 가야될 수 저장
                l_jump = go * -1
                # 만약 idx가 범위를 벗어나지 않았다면
                if 0 <= idx < len(field):
                    result += field[idx]  # 결과 값에 반영
                # 범위를 벗어났으면 종료
                else:
                    break
                # 점프 수 1회 감소
                K -= 1
    # 테케와 함께 누적합 출력
    print(f'#{test_case} {result}')