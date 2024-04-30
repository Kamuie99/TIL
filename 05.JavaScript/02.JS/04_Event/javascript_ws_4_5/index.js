// 가위, 바위, 보를 숫자로 변환
const ROCK = 0;
const SCISSORS = 1;
const PAPER = 2;

// 버튼 요소들 선택
const scissorsBtn = document.getElementById('scissors-button');
const rockBtn = document.getElementById('rock-button');
const paperBtn = document.getElementById('paper-button');

// 가위, 바위, 보 버튼 클릭 이벤트 핸들러 등록
scissorsBtn.addEventListener('click', () => buttonClickHandler(SCISSORS))
rockBtn.addEventListener('click', () => buttonClickHandler(ROCK))
paperBtn.addEventListener('click', () => buttonClickHandler(PAPER))

// 가위, 바위, 보 버튼 비활성화 함수
const disableBtns = () => {
  scissorsBtn.disabled = true;
  rockBtn.disabled = true;
  paperBtn.disabled = true;
}

// 가위, 바위, 보 버튼 활성화 함수
const enableBtns = () => {
  scissorsBtn.disabled = false;
  rockBtn.disabled = false;
  paperBtn.disabled = false;
}

// changeImg 함수
const changeImg = (what, where) => {
  if (where === 1) {
    what.src = './img/scissors.png';
  } else if (where === 0) {
    what.src = './img/rock.png';
  } else if (where === 2) {
    what.src = './img/paper.png';
  }
}


// modal 표시 함수
const showResult = (result) => {
  const resultMessage = document.querySelector('.modal-content');
  if (result === 1) {
    resultMessage.textContent = 'Player 1 Wins!';
  } else if (result === 2) {
    resultMessage.textContent = 'Player 2 Wins!';
  } else {
    resultMessage.textContent = "It's a tie!";
  }

  // modal 보이기
  const modal = document.querySelector('.modal');
  modal.style.display = 'flex';

  // 3초 후에 modal 숨기기
  setTimeout(() => {
    modal.style.display = 'none';
  }, 3000);
}

// playGame함수
const playGame = (player1, player2) => {
  if (player1 === player2) {
    return 0; // 무승부
  } else if (
    (player1 === ROCK && player2 === SCISSORS) ||
    (player1 === SCISSORS && player2 === PAPER) ||
    (player1 === PAPER && player2 === ROCK)
  ) {
    return 1; // player1 승리
  } else {
    return 2 // player2 승리
  }
}

// buttonClickHandler 함수
const buttonClickHandler = (choice) => {
  // 버튼 비활성화
  disableBtns();

  // 선택을 이미지에 반영
  const player1Img = document.getElementById('player1-img');
  changeImg(player1Img, choice)

  // 가능한 선택지 배열
  const choices = [ROCK, SCISSORS, PAPER];

  // 무작위 인덱스 선택
  let randomIndex = Math.floor(Math.random() * 3);

  // player2의 선택을 주기적으로 변경하기 위한 setInterval
  const interval = setInterval(() => {
    // 이미지 변경
    // console.log(choices[randomIndex]);
    const player2Img = document.getElementById('player2-img');
    changeImg(player2Img, choices[randomIndex])
    randomIndex = (randomIndex + 1) % 3;
  }, 100);

  // 결과를 3초 후에 화면에 표시
  setTimeout(() => {
    // clearInterval로 setInterval 중단
    clearInterval(interval);

    // 마지막 player2의 최종 선택을 저장
    const player2Choice = choices[randomIndex];

    // player2의 최종 선택 이미지 표시
    const player2Img = document.getElementById('player2-img');
    changeImg(player2Img, player2Choice);

    // 게임 결과 계산
    const result = playGame(choice, player2Choice);

    // 결과에 따라 승자 표시 및 점수 증가
    const countA = document.querySelector('.countA');
    const countB = document.querySelector('.countB');
    if (result === 1) {
      countA.textContent = parseInt(countA.textContent) + 1;
    } else if (result === 2) {
      countB.textContent = parseInt(countB.textContent) + 1;
    }

    // 결과 메시지 표시
    showResult(result);

    // 가위, 바위, 보 버튼 다시 활성화
    enableBtns();
  }, 3000);
}


