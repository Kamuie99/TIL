const citiesInfo = [
  {
    city: '서울',
    utcOffset: ['한국 표준시', 'KST', 'UTC+9'],
    latitude: 37,
    longitude: 126
  },
  {
    city: '도쿄',
    utcOffset: ['일본 표준시', 'JST', 'UTC+9'],
    latitude: 35,
    longitude: 139
  },
  {
    city: '상하이',
    utcOffset: ['중국 표준시', 'CST', 'UTC+8'],
    latitude: 31,
    longitude: 121
  }
]

citiesInfo.forEach(city => {
  for (key in city) {
    if (key === 'city') {
      console.log(`수도 : ${city[key]}`)
    }
    else if (Array.isArray(city[key])) {
      console.log(`${key} : ${city[key][city[key].length - 1]}`)
    }
    else {
      console.log(`${key} : ${city[key]}`)
    }
  }
});


const studentNames = ["John", "Alice", "Bob"];
const studentAges = {
  John: 50,
  Alice: 100,
  Bob: 25,
};

studentNames.forEach(student => {
  if (studentAges[student] >= 50) {
    console.log(`${student}은 ${studentAges[student]}세 입니다.`)
  }
})

for (student of studentNames) {
  if (studentAges[student] >= 50) {
    console.log(`${student}은 ${studentAges[student]}세 입니다.`)
  }
}
