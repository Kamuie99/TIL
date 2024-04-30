### ECMAScript

- Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
- 스크립트 언어가 준수해야 하는 규칙, 세부사항 등을 제공
- ECMAScript는 JS의 표준이며, JS는 ECMAScript 표준을 따르는 구체적인 프로그래밍 언어

### DOM

- Document Object Model
- 웹 페이지를 구조화된 객체로 제공하여 페이지 구조에 접근할 수 있는 방법 제공
- **DOM 선택**
    - document.querySelector() : 요소 한 개 선택
    - document.querySelectorAll() : 요소 여러 개 선택
- **속성 조작**
    - element.classList.add() : 지정한 클래스 값 추가
    - element.classList.remove() : 지정한 클래스 값을 제거
    - elemnet.classList.toggle() : 클래스가 존재한다면 제거하고 false 반환, 존재하지 않는다면 클래스를 추가하고 true를 반환
    - element.getAttribute() : 해당 요소에 지정된 값을 반환(조회)
    - element.setAttribute(name, value) : 지정된 요소의 속성 값을 설정
    - element.removeAttribute() : 요소에서 지정된 이름을 가진 속성 제거
- **HTML 조작**
    
    ```jsx
    const content = document.querySelector('.className')
    console.log(content.textContent) // content 안의 내용
    content.textContent = '내용을 수정했습니다'
    console.log(content.textContent) // 내용을 수정했습니다.
    
    ```