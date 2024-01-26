############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 max() 사용 시 감점
def max_score(score_list):

    #-------- test_case_01 --------#
    # max_num = 0
    # for score in score_list:
    #     if score > max_num:
    #         max_num = score
    # return max_num
    #-------- test_case_02 --------#
    # 인자로 전달 받은 함수를 오름차순 정렬
    score_list.sort()
    # 정렬된 배열의 마지막 수가 큰 수, 그 수를 변수에 저장
    max_score = score_list[-1]
    # 해당 변수 return
    return max_score

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]
print(max_score(scores1)) # 90
#####################################################