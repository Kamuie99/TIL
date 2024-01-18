matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.

# len 사용하지 않고 matrix 총 길이 matrix 변수에 담고 출력
matrix_len = 0

for i in matrix:
    matrix_len += 1

print(matrix_len)

# len 사용하지 않고, matrix가 가진 각 요소의 길이 출력
for row in matrix:
    temporary_len = 0
    for number in row:
        temporary_len += 1
    if temporary_len <= 4:
        print(f"{row} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.")

# range와 len을 사용하여 matrix와 matrix가 가진 각 리스트들의 인덱스를 기준으로 순회할 수 있도록 for문 작성
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(f'matrix의 {x}, {y} 번째 요소의 값은 {matrix[x][y]}입니다.')
