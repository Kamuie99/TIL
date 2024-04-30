const accounts = [
  { name: 'sophia', balance: 1200 },
  { name: 'john', balance: 50000 },
  { name: 'tailer', balance: 24000 }
]
const newAccount = accounts.find(account => account.balance === 24000)
console.log(newAccount)