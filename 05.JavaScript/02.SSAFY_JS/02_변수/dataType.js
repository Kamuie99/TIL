// 원시 자료형 변수에 할당될 때 값이 복사됨
// 변수 간에 서로 영향을 미치지 않음
const bar = 'bar'
upperBar = bar.toUpperCase()

console.log(bar) // bar
console.log(upperBar) // BAR

// 참조 자료형은 객체를 생성하면 객체의 메모리 주소를 변수에 할당
// 변수 간에 서로 영향을 미침
const obj1 = {name: 'Alice', age: 30}
const obj2 = obj1
obj2.age = 40

console.log(obj1.age) // 40
console.log(obj2.age) // 40

// 템플릿 리터럴
const age = 100
const message = `홍길동은 ${age}세 입니다.`
console.log(message); // 홍길동은 100세 입니다.

// null과 undefined
let a = null
let b
console.log(a) // null
console.log(b) // undefined
console.log(typeof a)