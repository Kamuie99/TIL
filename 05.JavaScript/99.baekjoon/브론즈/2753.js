const input = require('fs').readFileSync('input.txt', 'utf-8').trim();
const inputYear = Number(input);

const checkYoonNyun = (year) => {
  if ((year % 4 === 0 && year % 100 != 0) || year % 400 === 0) {
    console.log(1)
  } else {
    console.log(0)
  }
}

checkYoonNyun(inputYear);