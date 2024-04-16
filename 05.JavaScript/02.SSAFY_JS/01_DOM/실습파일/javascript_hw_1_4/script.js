const name = document.querySelector("#name");
const job = document.querySelector("#job");
const experience = document.querySelector("#experience");
const email = document.querySelector("#email");
const phone = document.querySelector("#phone");

name.textContent = "홍길동";
job.textContent = "의적";
experience.textContent = "서당";
email.textContent = "hgd@korea";
phone.textContent = "010-1234-1234";

const img = document.querySelector("img");
img.setAttribute("src", "profile.jpg");
img.setAttribute("alt", "프로필 사진");

////////////////////////////////// hw_1_4 ////////////////////////////////////

// body 태그를 선택하여 container 클래스를 부여한다.
const body = document.querySelector('body');
body.classList.add('container');

// h1 태그를 선택하여 title class를 부여한다.
const h1 = document.querySelector('h1');
h1.classList.add('title');

// img 태그에 img class를 부여한다.
img.classList.add('img');

// id가 name, job, experience, email, phone인 요소에 highlight class를 부여한다.
const updates = ['name', 'job', 'experience', 'email', 'phone'];
for (let updateId of updates) {
  const element = document.querySelector(`#${updateId}`)
  element.classList.add('highlight');
};

// 연락처 정보 하단에 SNS 정보를 추가하시오.
const sns = document.createElement('p');
sns.innerHTML = 'SNS: <b class="highlight">dakgoo02@sns.com</b>';
body.appendChild(sns);

// const sns = document.createElement('p');
// sns.textContent = 'SNS: ';
// body.appendChild(sns);

// const snsContent = document.createElement('b');
// snsContent.textContent = 'dakgoo02@sns.com';
// snsContent.classList.add('highlight');
// sns.appendChild(snsContent);
