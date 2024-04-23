# JS - 동기, 비동기

### Synchronous(동기)

- 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식

```jsx
console.log('첫번째 작업')
for (let i=0; i<10; i++) {
	console.log('메인작업')
}
console.log('마지막 작업')
```

- 메인 작업이 모두 수행되어야 마지막 작업이 수행됨

### Asynchronous(비동기)

- 작업의 완료 여부를 신경 쓰지 않고 **동시에 다른 작업들을 수행할 수 있음**

```jsx
const slowRequest = function (callBack) {
	console.log('1. 오래 걸리는 작업 시작 ... ')
	setTimeout = () => {
		callBack()
	}, 3000)
}

const myCallBack = function () {
	console.log('2. 콜백함수 실행됨')
}

slowRequest(myCallBack)

console.log('3. 다른 작업 실행')

// 출력결과
1. 오래 걸리는 작업 시작 ...
3. 다른 작업 실행
2. 콜백함수 실행됨
```

- 병렬적 수행
- 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

### 브라우저 환경에서의 JS 비동기 처리 동작 방식

- 모든 작업은 **Call Stack**으로 들어간 후 처리된다.
- 오래 걸리는 작업이 Call Stack 으로 들어오면 Web API로 보내 별도로 처리하도록 한다.
- Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue에 순서대로 들어간다.
- Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된 작업을 Call Stack 으로 보낸다.

### 정리

- JS는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 진행
- 하지만 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 됨