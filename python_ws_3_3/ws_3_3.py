def rental_book(name, num):
    decrease_book(num)
    print(f"남은 책의 수 : {number_of_book}")
    print(f"{name}님이 {num}권의 책을 대여하였습니다.")

number_of_book = 100

def decrease_book(num):
    global number_of_book
    number_of_book -= num
    return number_of_book

rental_book('홍길동', 3)