// 아래에 코드 작성
const person = {
  name: 'Alice',
  age: 30,
  city: 'New York',
  introduce() {
    return `안녕하세요 ${this.city}에 거주하는 ${this.age}살 ${this.name}입니다.`
  }
}

const printPersonInfo = (person) => {
  const { name, age, city } = person
  console.log(`${name} / ${age} / ${city}`)
}

// 메서드 및 함수 호출
console.log(person.introduce())  // 안녕하세요 New York에 거주하는 30살 Alice입니다.
printPersonInfo(person)  // Alice / 30 / New York