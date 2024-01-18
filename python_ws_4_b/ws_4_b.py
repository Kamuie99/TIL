food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

# for item in food_list:
#     # 만약, 이름이 토마토라면 종류를 과일로 변경하고 출력
#     if item['이름'] == '토마토':
#         item['종류'] = '과일'
#         print(f"{item['이름']} 은/는 {item['종류']}이다.")
#     elif item['이름'] == '자장면':
#         # 만약, 이름이 자장면이라면 자장면엔 고춧가루지 출력
#         print(f"{item['이름']}엔 고춧가루지")
#         print(f"{item['이름']} 은/는 {item['종류']}이다.")
#     else:
#         print(f"{item['이름']} 은/는 {item['종류']}이다.")

# 추가) for문으로 작성한 코드를 while문으로 변경한다.
# index 값을 0으로 설정
index = 0
while index < len(food_list):
    item = food_list[index]
    # 만약, 이름이 토마토라면 종류를 과일로 변경하고 출력
    if item['이름'] == '토마토':
        item['종류'] = '과일'
        print(f"{item['이름']} 은/는 {item['종류']} (이)다.")
    elif item['이름'] == '자장면':
        # 만약, 이름이 자장면이라면 자장면엔 고춧가루지 출력
        print(f"{item['이름']}엔 고춧가루지")
        print(f"{item['이름']} 은/는 {item['종류']} (이)다.")
    else:
        print(f"{item['이름']} 은/는 {item['종류']} (이)다.")
    # 조건문 통과 후 index 값 1 증가, 3이 되면 종료
    index += 1

# 반복문이 끝난 후, food_list 출력
print(food_list)