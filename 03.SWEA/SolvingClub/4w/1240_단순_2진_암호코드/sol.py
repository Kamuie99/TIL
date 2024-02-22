import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    # 배열의 세로 크기 N과 가로크기 M을 입력 받는다.
    N, M = map(int, input().split())
    # field 2차원 배열에 일단 다 넣어 놓기
    field = [list(map(int, input())) for i in range(N)]
    # 0부터 9까지의 암호 코드를 인덱스 번호:암호규칙으로 배열에 저장
    codes = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    
    # 0으로만 이루어진 가로줄은 필요없으니까 어느 줄 부터 필요한 자료인지 확인
    data_idx = []
    for i in range(N):
        if 1 in field[i]:
            data_idx.append(i)
            
    # 필요한 자료들만 일단 data_list에 저장한다. (0으로만 이루어진 가로줄 삭제)
    data_list = []
    for d in data_idx:
        data_list.append(field[d])
        
    # 가로줄에서 값을 하나씩 확인해가면서 어디부터 잘라야 될지 판단
    start_idx = 0
    for i in range(M-7):
        temp = ''.join(str(s) for s in data_list[0][i:7+i])
        # 만약 자른 부분이 codes 안에 있고, 자른부분의 마지막이 1로 끝난다면
        if temp in codes and data_list[0][i+55] == 1:
            # 해당 부분을 자르기로 결정하고 break
            start_idx = i
            break
    
    # 해독할 코드를 일단 code에 담아서 coding 안에 자른 암호들을 저장
    code = data_list[0][start_idx:56+start_idx]
    coding = []
    for i in range(0, len(code) , 7): 
        temp = ''.join(str(s) for s in code[i:7+i])
        coding.append(temp)
    
    # c 안에 암호를 해독한 결과(숫자값)들을 저장
    c = [] 
    for cod in coding:
        temp = codes.index(cod)
        c.append(temp)
    
    # 해당 검증코드가 맞는지 확인 
    test = (c[0] + c[2] + c[4] + c[6]) * 3 + c[1] + c[3] + c[5] + c[7]
    # 만약 10의 배수이면 암호코드에 포함된 숫자의 합을 테케와 함께 출력
    if test % 10 == 0:
        print(f'#{test_case} {sum(c)}')
    # 만약 잘못된 암호코드일 경우 대신 0을 출력
    else:
        print(f'#{test_case} {0}')