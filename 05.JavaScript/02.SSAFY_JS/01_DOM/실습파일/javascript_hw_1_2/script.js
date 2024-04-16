const name = document.querySelector('#name');
const job = document.getElementById('job');
const experience = document.getElementById('experience');
const email = document.getElementById('email');
const phone = document.getElementById('phone');

name.textContent = '이유찬';
job.textContent = '학생';
experience.textContent = '백수 24년 경력';
email.textContent = 'dakgoo02@naver.com';
phone.textContent = '010-1234-5678';

const img = document.querySelector('img');
img.setAttribute('src', 'profile.jpg');
img.setAttribute('alt', 'profile');

const updates = {
  'name' : '이유찬',
  'job': '학생',
  'experience': '백수 23년 경력',
  'email': 'dakgoo02@naver.com',
  'phone': '010-1234-5678'
};

for (let key in updates) {
  console.log(key)
  const value = updates[key];
  // document.getElementById(key).textContent = value;
  document.querySelector(`#${key}`).textContent = value;
}

