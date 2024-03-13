import random

# 우리반 학생 전체 명단 리스트 만들기

students = ['강현성', '김송희', '박재현', '구현우', '이권민', '김동현',
            '정  훈', '박지원', '이승민', '차민주', '이창호', '김구태',
            '김종덕', '최지우', '이유찬', '김동환', '박동현', '이승지',
            '임경태', '윤예리', '허유정', '어지민', '장효승', '박수빈']


# 리스트 무작위로 섞어주는 라이브러리 사용
random.shuffle(students)

# 방명록 당첨자 뽑기
# print(f"방명록  랜덤 당첨자는: {students[0]}")
# print("축하드립니다! 적극적인 참여 감사합니다! ")



# 스크린 방향과 교수님 자리 표시
print("{}  스크린  {}".format("="*18, "="*18))
print("{} 교수님".format(" "* 39))
print("")

# # 무작위로 섞은 리스트를 하나씩 출력
# count = 0
# for student in students:
#     print("{:<3}".format(student), end=" ")
#     count+=1
#     if count == 3:
#         print("", end="     ")
#     elif count == 6:
#         print(" ")
#         count = 0

print(students)





# ctrl + alt + 방향키 위, 아래 | 포커싱 증가
# ctrl + 왼쪽, 오른쪽 방향키
# alt + 방향키 | 포커싱 되어있는 줄 위치 이동
        
# alt + shift + 위 아래 방향키 | 포커싱 되어 있는 줄 복제
# ctrl 누르고 움직이면 단어 별로 움직여짐
