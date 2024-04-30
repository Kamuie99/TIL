const createPerson = (name, age, city) => {
  return {
    name,
    age,
    [`livesIn${city}`]: city ? true : false,
    greeting() {
      console.log(name, age)
    },
  }
}

const person1 = createPerson('홍길동', 30, '')
console.log(person1) // {name: '홍길동', age: 30, livesIn옥천: true, greeting: ƒ}
person1.greeting() //