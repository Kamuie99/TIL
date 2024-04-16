const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split(' ');

const a = parseInt(input[0]);
const b = parseInt(input[1]);

if (a > b) {
  console.log('>');
} else if (a == b) {
  console.log('==');
} else {
  console.log('<');
};


