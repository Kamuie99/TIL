// 선언식
// 1. 익명함수 사용 불가능
// 2. 호이스팅 있음
function add(num1, num2) {
  return num1 + num2
}

// 표현식
// 1. 익명함수 사용 가능
// 2. 호이스팅 없음
const myFunc = function (x, y, z) {
  return x + y + z
}

// 화살표 함수
const myFunc2 = (x, y, z) => x + y + z  // {return x + y + z}

// ...은 전개구문
let numbers = [1, 2, 3]
console.log(myFunc(...numbers)) // 6 
console.log(myFunc2(...numbers)) // 6

// 객체 단축속성
function createPerson(name, age, city) {
  return {
    name,
    age,
    [`livesIn${city}`]: city ? true : false, // 계산된 속성 이름?
    greeting() {
      console.log(`${this.name}의 나이는 ${this.age}입니다. `)
    }
  }
}

// age 배열 순회하여 값이 20 미만인 경우만 출력하는 코드
ages.forEach((age) => {
  if (age < 20) {
    console.log(age)
  }
})

// actors 배열 순회하면서 20 이상인 객체만 모아 새로운 배열 생성
let adult_actors = actors.filter(actor => actor.age >= 20);


