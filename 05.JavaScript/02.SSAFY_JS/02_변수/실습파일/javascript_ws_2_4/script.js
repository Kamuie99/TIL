const roles = ['주연배우', '조연배우', '주연배우', '우정출연', '우정출연', '조연배우']
const names = ['홍길동', '이춘향', '금나래', '장보고', '임꺽정', '강감찬']

let length = 0;
for (role of roles) {
  length++
}

for (let i = 0; i < length; i++) {
  if (roles[i] === '주연배우') {
    console.log(`주연배우 : ${names[i]}님 반갑습니다!`)
  } else if (roles[i] === '조연배우') {
    console.log(`${names[i]}님 환영합니다!`)
  } else if (roles[i] === '우정출연') {
    console.log(`${names[i]}님 와 주셔서 감사합니다!`)
  }
}