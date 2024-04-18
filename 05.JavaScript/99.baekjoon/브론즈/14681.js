const input = require('fs').readFileSync('input.txt', 'utf-8').trim().split('\n');
const x = parseInt(input[0])
const y = parseInt(input[1])

const where = (x, y) => {
  if (x > 0 && y > 0) return 1
  else if (x < 0 && y > 0) return 2
  else if (x < 0 && y < 0) return 3
  else if (x > 0 && y < 0) return 4
}

console.log(where(x, y))