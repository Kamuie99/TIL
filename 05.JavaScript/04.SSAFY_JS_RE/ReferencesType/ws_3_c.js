const students = [
  { name: 'Alice', scores: [85, 90, 95] },
  { name: 'Bella', scores: [50, 80, 80] },
  { name: 'Caley', scores: [90, 55, 35] },
  { name: 'Dave', scores: [100, 100, 100] },
  { name: 'Eve', scores: [88, 90, 92] }
]

const makeAvgScores1 = (students) => {
  let result = {}
  for (let i = 0; i < students.length; i++) {
    const tempArray = students[i].scores
    let count = 0;
    let hab = 0;
    for (temp of tempArray) { count += 1; hab += temp }
    result[students[i].name] = hab / count
    // console.log(`${students[i].name}: ${hab / count}`)
  }
  return result
}
console.log(makeAvgScores1(students))
