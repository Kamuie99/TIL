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

for (const info of citiesInfo) {
  let printkey; let printvalue;
  for (key in info) {
    (key === 'city' ? printkey = '수도' : printkey = key);
    (Array.isArray(info[key]) ? printvalue = info[key][2] : printvalue = info[key]);
    console.log(`${printkey} : ${printvalue}`);
  }
  console.log();
}