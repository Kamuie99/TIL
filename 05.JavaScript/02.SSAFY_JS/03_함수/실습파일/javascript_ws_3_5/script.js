function createPerson(name, age, city) {
  return {
    name,
    age,
    [`livesIn${city}`]: city ? true : false,
    greeting() {
      console.log(`${this.name}의 나이는 ${this.age}입니다. `)
    }
  }
}

const person1 = createPerson('홍길동', 30, '옥천')
console.log(person1) // {name: '홍길동', age: 30, livesIn옥천: true, greeting: ƒ}
person1.greeting() // 홍길동의 나이는 30입니다.