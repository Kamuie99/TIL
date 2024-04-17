const students = [
  { name: 'Alice', scores: [85, 90, 95] },
  { name: 'Bella', scores: [50, 80, 80] },
  { name: 'Caley', scores: [90, 55, 35] },
  { name: 'Dave', scores: [100, 100, 100] },
  { name: 'Eve', scores: [88, 90, 92] }
]
// 아래에 코드 작성
const makeAvgScores1 = (students) => {
  let result = {};
  for (let i = 0; i < students.length; i++) {
    let name = students[i].name
    let score = students[i].scores
    let tmp = 0;
    for (let j = 0; j < score.length; j++) {
      tmp += score[j]
    }
    let studnetAvg = tmp / score.length
    result[name] = studnetAvg
  }
  return result
}

const makeAvgScores2 = (students) => {
  let result = {};
  for (let student of students) {
    let sum = 0;
    const name = student.name
    const length = student.scores.length;
    for (let score of student.scores) {
      sum += score
    }
    result[name] = sum / length
  }
  return result
}

const makeAvgScores3 = (students) => {
  let result = {};
  students.forEach(student => {
    let sum = 0;
    const name = student.name;
    const length = student.scores.length;
    student.scores.forEach(score => {
      sum += score;
    });
    result[name] = sum / length;
  });
  return result;
}


// 함수 호출
const result1 = makeAvgScores1(students)
const result2 = makeAvgScores2(students)
const result3 = makeAvgScores3(students)
console.log(result1)
console.log(result2)
console.log(result3)