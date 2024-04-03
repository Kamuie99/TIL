# React, JSX, Component

### ➡️ **React**

- **What?**  JavaScript 라이브러리, **오직 V(iew)만 신경 쓰는** 라이브러리
- **How?**  Virtual **D**ocument**O**bject**M**odel을 사용, DOM은 트리 구조로 구성
- **DOM?**  객체로 문서 구조를 표현하는 방법
- **Why?**  업데이트 처리 간결성, UI 업데이트 복잡함 감소, UserExperience 환경 개선

```jsx
yarn create react-app <앱 이름>    or     npm init react-app <앱 이름>

$ cd <앱 이름>
$ yarn start or npm start
```

### ➡️ **JSX**

- **JSX 문법**
1. **감싸는 요소:** 컴포넌트는 반드시 하나의 부모요소로 감쌀 것
2. **모든 태그**(input, button 등도 포함)는 반드시 닫을 것       ex) <input />
3. If문 대신 **조건부 연산자** 사용

```jsx
<div> { a===b ? (<h1>참입니다</h1>) : (<h1>거짓입니다</h1>) } </div>
```

1. undefined를 렌더링 하지 않기
2. class 대신 className, inline style에서 ‘-’ 대신 CamelCase로 사용

```jsx
function App() {
	const name = '이유찬';
	const style = {
		backgroundColor : 'black',
		fontSize : '48px',
	};
	return <div style={style} className="react">{name}</div>;
}

export defaul App;

{/* 6. 주석은 이와 같이 이용한다. */}
```

### ➡️ Component

- **What?**  **단순한 템플릿을 넘어**, 데이터가 주어졌을 때 이에 맞추어 UI를 만들어줌
- **How?**  라이프사이클 API를 이용, 컴포넌트의 변화에 따라 작업처리 가능
- **Class형 Component**
    - state 기능 및 라이프 사이클 기능 사용가능, 임의 메서드 정의 가능
    - render 함수가 반드시 필요, JSX를 반환
- **함수형 Component**
    - 선언하기 편하고, 메모리 자원을 절약할 수 있다.
    - ~~state와 라이프 사이클 API 사용이 불가능하다.~~
    - v16.8 업데이트 이후 **Hooks로 위의 기능을 대체**할 수 있게 되었다.
- **props**
    - properties를 줄인 표현, 컴포넌트 속성 설정에 사용하는 요소
    - 부모 컴포넌트(App.js)에서 설정 가능
- **prop-Types**
    - 컴포넌트의 필수 props를 지정, type을 지정할 때 사용
    - 반드시 사용하지는 않지만, 협업 시 필요한 props를 쉽게 알 수 있어서 유용하다.