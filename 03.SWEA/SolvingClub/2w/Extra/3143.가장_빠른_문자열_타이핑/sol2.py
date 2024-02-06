import sys
sys.stdin = open('input.txt')

T = int(input())
for テストケース in range(1, T+1):
    total, 探す = map(str, input().split())
    カウント = total.count(探す)
    テスト = len(total) - (カウント * len(探す)) + カウント
    print(f'#{テストケース} {テスト}')