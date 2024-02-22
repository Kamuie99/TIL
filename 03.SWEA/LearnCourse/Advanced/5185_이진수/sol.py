import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # N과 16진수 값을 입력 받는다.
    N, hex_value = map(str, input().split())
    # 각 16진수 문자를 4비트 이진수로 변환한 뒤
    # 이진수를 리스트 형태로 만들고 문자열로 반환
    result = ''.join(format(int(c, 16), '04b') for c in hex_value)
    # 테케와 함께 결과값 출력
    print(f'#{test_case} {result}')
