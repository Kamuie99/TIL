const input = require('fs').readFileSync('input.txt', 'utf-8').trim();
const N = Number(input);

if (90 <= N && N <= 100) {
  console.log('A')
} else if (80 <= N && N <= 89) {
  console.log('B')
} else if (70 <= N && N <= 79) {
  console.log('C')
} else if (60 <= N && N <= 69) {
  console.log('D')
} else {
  console.log('F')
}