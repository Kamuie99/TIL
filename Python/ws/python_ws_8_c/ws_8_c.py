class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        self.author = author
        super().__init__(data_type, title, content, created_at, updated_at)
    
class Other(BaseModel):
    TYPE = 'Other Model'

    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
print('Novel 모델 인스턴스의 PK와 save 메서드')
