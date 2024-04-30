const headerTag = document.querySelector('header');
const nowId = headerTag.getAttribute('id');

headerTag.classList.add(nowId);
headerTag.removeAttribute('id');

const img = document.querySelector('img');
img.setAttribute('src', 'book.png');