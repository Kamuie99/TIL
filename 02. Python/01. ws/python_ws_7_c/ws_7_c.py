class Car:
    
    wheels = 4
    # 아래에 코드를 작성하시오.
    def __init__(self, engine, driving_system, sound):
        self.engine = engine
        self.driving_system = driving_system
        self.sound = sound
    
    def drive(self):
        print(self.sound)
        return self.engine

    def introduce(self):
        print(f'제 차의 엔진은 {self.engine} 방식이고, {self.driving_system} (으)로 동작합니다.')

    @staticmethod
    def description():
        return "자동차는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통 수단이다."


    @classmethod
    def increase_wheels(cls):
        cls.wheels += 1
        print('법이 개정되어 모든 자동차의 필요 바퀴 수가 1증가하였습니다.')


car1 = Car('gasoline', '후륜구동', '부릉부릉')
car2 = Car('diesel', '전륜구동', '달달달달')
car3 = Car('hybrid', '4wd', '슈웅')

car1.drive()
print(car2.drive())

print('===')
car1.introduce()
car3.introduce()

print('===')
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
Car.increase_wheels()
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')


# Q1. 오늘자 실습 Lv.3 문제인 자동차 클래스 정의하기에서
# 모든 자동차들이 공통으로 가질 클래스 변수 wheels를 정의
# 하고 4를 할당한다. 라고 할 때 wheels 라는 클래스 변수를
# 정의하고 클래스 메서드로 모든 인스턴스에서 동일한 wheels
# 값이 공유 되도록 했는데, 해당 문제가 이렇게 접근하는게
# 맞는지 여쭤봐도 되겠습니까?

# Q2. 이 경우에는 다른 자동차 car4를 만들어도 바퀴 값은 5가
# 기본값이 되어 car4도 5의 바퀴를 가진 객체가 되나요?