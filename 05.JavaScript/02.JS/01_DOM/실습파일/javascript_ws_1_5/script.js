//////////////// section 요소와 article 요소를 선택한다. ////////////////
const sectionTag = document.querySelector('section');
const articleTag = document.querySelector('article');

/////////// 새 article 요소와 그 하위 요소를 생성한다. //////////////
const newArticle = document.createElement('article');
const newdivTag = document.createElement('div');
newArticle.appendChild(newdivTag);

/////////// 새 article 요소와 하위 요소에 클래스 등 속성과 값을 추가한다.///////////
const newh5Tag = document.createElement('h5');
const newpTag = document.createElement('p');
newdivTag.appendChild(newh5Tag);
newdivTag.appendChild(newpTag);

// 원래 클래스명을 가져온다.
const divTag = document.querySelector('div');
const h5Tag = document.querySelector('h5');
const pTag = document.querySelector('p');

// 새로만든 article 태그에 원래 클래스 가져와서 추가, 스타일도 가져와서 추가
const articleClass = articleTag.getAttribute('class');
newArticle.classList.add(articleClass);
const articleStyle = articleTag.getAttribute('style');
newArticle.setAttribute('style', articleStyle);

// 새로만든 div 태그에 원래 클래스 가져와서 추가
const divClass = divTag.getAttribute('class');
newdivTag.classList.add(divClass);

// 새로만든 h5 태그에 원래 클래스 가져와서 추가, 내용 작성
const h5Class = h5Tag.getAttribute('class');
newh5Tag.classList.add(h5Class);
newh5Tag.textContent = '카드 제목';

// 새로만든 p 태그에 원래 클래스 가져와서 추가, 내용 작성
const pClass = pTag.getAttribute('class');
newpTag.classList.add(pClass);
newpTag.textContent = '카드 내용';


//////////////////////// section에 새로 작성한 article을 추가한다.
sectionTag.appendChild(newArticle);

/////////////////////// 기존의 article 요소는 삭제한다.
articleTag.remove();