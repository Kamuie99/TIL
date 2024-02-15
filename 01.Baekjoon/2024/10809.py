from string import ascii_lowercase
# 알파벳 리스트 만들기
alphabet_list = list(ascii_lowercase)   # 26개의 알파벳이 다 들어가있는 배열
# 단어 S 입력 받기
S = input()
# 결과들을 담을 배열 생성
results = []
# 해당 알파벳이 있으면 인덱스값 results 배열에 추가, 없으면 -1을 추가
for alpha in alphabet_list:
    if alpha in S:
        results.append(S.index(alpha))
    else:
        results.append(-1)
# results 배열의 요소들을 다 출력하기
print(*results)