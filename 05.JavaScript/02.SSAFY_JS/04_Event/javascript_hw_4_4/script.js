const form = document.querySelector('form')

function addTodo(event) {
  // 이벤트를 취소한다.
  event.preventDefault()

  // 입력 element를 찾고 해당 입력 element의 value 값을 저장한다.
  const inputTag = document.querySelector('input')
  const inputData = inputTag.value
  if (inputData.trim()) {
    // li element를 생성 후 input element의 value 값을 데이터로 저장한다
    const liTag = document.createElement('li')
    liTag.textContent = inputData

    // ul 태그의 자식 태그로 위에서 생성한 li element를 넣는다.
    const ulTag = document.querySelector('ul')
    ulTag.appendChild(liTag)
    inputTag.value = '' // todo 추가 후 input의 입력 데이터는 초기화
    // 삭제 버튼을 생성 후 li 태그의 자식 태그로 넣는다.
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'X'
    liTag.appendChild(deleteBtn)

    // 삭제 버튼을 클릭하면 해당 li element를 삭제한다
    deleteBtn.addEventListener('click', () => {
      liTag.remove(liTag)
    })

    // li element를 클릭하면 취소선이 토글된다.
    liTag.addEventListener('click', () => {
      liTag.classList.toggle('done')
    })
  } else {
    alert('할 일을 입력하세요..')
  }
}

form.addEventListener('submit', addTodo)