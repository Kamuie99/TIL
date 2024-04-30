const scores = [90, 80, 70, 60, 40]
// for .. of 문으로 코드 작성
// 1) 주어진 배열 scores의 길이를 length 변수에 할당, 출력
const length = scores.length;
console.log(length);
// 2) 주어진 배열 scores가 가진 요소들의 총 합을 계산, 출력
let sum = 0;
for (score of scores) {
  sum += score;
};
console.log(sum);
// 3) scores가 가진 요소들의 평균 값을 출력하시오
console.log(sum / length);
// while문으로 코드 작성
// 4) length를 활용하여 scores 배열의 요소들을 역순으로 출력
for (i = length - 1; i >= 0; i--) {
  console.log(scores[i]);
};
