// forEach와 map의 차이
const array1 = [1, 2, 3, 4, 5]
const result = []

// forEach는 반환값이 없다.
console.log(array1.forEach(element => {
  result.push(element * 2)
}));
console.log(result) // [2, 4, 6, 8, 10]

// map은 여러번 반복할 때 유리하다. 반환값이 있다.
console.log(array1.map(e => e * 2)) // [2, 4, 6, 8, 10]

// 구조 분해 할당을 사용하여 객체에서 key값만 뽑아서 개별 변수에 할당
const student = {
  Name: 'Lee',
  age: 26,
  major: 'Japanese'
}
const { age } = student // const age = student.age

