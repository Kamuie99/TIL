// 반 학생들의 이름이 담긴 배열
var students = ['강현성', '김송희', '박재현', '구현우', '이권민', '김동현',
  '정　훈', '박지원', '이승민', '차민주', '이창호', '김구태',
  '김종덕', '최지우', '이유찬', '김동환', '박동현', '이승지',
  '임경태', '윤예리', '허유정', '어지민', '장효승', '박수빈'];

// Fisher-Yates 알고리즘을 사용하여 배열 섞기
function shuffleArray(array) {
  for (var i = array.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
  return array;
}

// 학생 배열을 섞기
shuffleArray(students);

// HTML에 이름 삽입하는 함수
function insertNames(className, startIndex, endIndex) {
  var lines = document.getElementsByClassName(className);

  // lines는 HTMLCollection이므로 배열로 변환
  var linesArray = Array.from(lines);

  linesArray.forEach(function (line) {
    for (var i = startIndex; i <= endIndex; i++) {
      var div = document.createElement('div');
      div.textContent = students[i - 1];
      line.appendChild(div);
    }
  });
}

// 섞인 이름을 HTML에 삽입
insertNames('s_1', 1, 3);
insertNames('s_2', 4, 6);
insertNames('s_3', 7, 9);
insertNames('s_4', 10, 12);
insertNames('s_5', 13, 15);
insertNames('s_6', 16, 18);
insertNames('s_7', 19, 21);
insertNames('s_8', 22, 24);


// 새로고침 버튼 '센세'
document.getElementById('refreshButton').addEventListener('click', function () {
  location.reload();
});


