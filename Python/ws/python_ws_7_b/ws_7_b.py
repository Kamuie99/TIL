# 아래에 코드를 작성하시오.
class Myth:
    type_of_myth = 0

    def __init__(self, name):
        self.name = name
        Myth.type_of_myth += 1
    
    @staticmethod
    def description():
        return '신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.'

myth_instance1 = Myth('dangun')
print(myth_instance1.name)
myth_instance2 = Myth('greek & rome')
print(myth_instance2.name)


print(f'현재까지 생성된 신화 수: {Myth.type_of_myth}')
print(Myth.description())