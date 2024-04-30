const title = document.querySelector('.title');
title.textContent = '제목을 수정했습니다.';


const smallTitle = document.createElement('h2');
smallTitle.textContent = '소제목';


const divTag = document.querySelector('div');
divTag.appendChild(smallTitle);


divTag.style.color = 'crimson';
divTag.style.fontSize = '1rem';
divTag.style.border = '1px solid grey';


// divTag.removeChild(smallTitle);