const ages = [18, 20, 21, 29, 11, 31]
const names = ['홍길동', '이춘향', '금나래', '장보고', '임꺽정', '강감찬']
/*
  배열 ages를 순회하여 값이 20미만인 경우만 출력하는 코드를 작성하시오.
  forEach를 활용하여 구현한다.
  ex)
  18
  11
*/
ages.forEach((age) => {
  if (age < 20) {
    console.log(age)
  }
})
/*
  길이가 서로 같은 배열 ages와 names를 활용하여 새로운 배열 actors를 완성하시오.
  배열 actors는 age와 name을 키로 가지는 객체들로 구성한다.
  각 객체는 names와 ages의 요소들을 index 순으로 매칭시켜, 각각 name과 age 키에 할당하여 구성한다.
  ex)
  [        
    {age: 18, name: '홍길동'}
    {age: 20, name: '이춘향'}
    ...
  ]
*/
let actors = [];
const length = ages.length;
for (let i = 0; i < length; i++) {
  let temp = { age: ages[i], name: names[i] }
  actors.push(temp)
}
console.log(actors)
/*
  새롭게 생성한 배열 actors를 순회하여, age가 20 이상인 객체만 모아
  새로운 배열 adult_actors에 할당 하는 코드를 작성하시오.
  filter를 활용하여 구현한다.
  ex)
  [
    {age: 20, name: '이춘향'} 
    {age: 21, name: '금나래'}
    ...
  ]
*/
let adult_actors = actors.filter(actor => actor.age >= 20);
console.log(adult_actors)