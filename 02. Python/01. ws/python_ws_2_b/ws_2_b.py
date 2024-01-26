title = '딕셔너리 활용하기'
# 아래에 코드를 작성하시오.

# data 딕셔너리 만들기
data = {'과목' : 'Python', '구분' : '실습', '단계' : 2, '문제번호' : 3251, '이름' : None, '일차' : 22}
# data를 출력한다.
print(data)
# data 단계 key에 할당된 값을 2단계로 수정
data['단계'] = str(data['단계']) + '단계'
# data의 이름 key에 title 변수 할당
data['이름'] = title
# data의 일차 key에 할당된 값 -20 재할당
data['일차'] -= 20
# data 변수 출력
print(data)