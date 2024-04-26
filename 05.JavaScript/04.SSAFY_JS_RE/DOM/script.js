const container = document.createElement('div')
container.setAttribute('id', 'container')

const article = document.createElement('div')
article.classList.add('article')

const h1Tag = document.createElement('h1')
h1Tag.textContent = 'Article Title'

const pTag = document.createElement('p')
pTag.textContent = 'This is a article content'
pTag.style.cssText = `
  bodrer-top : 1px solid black;
  padding-top : 10px;
`

document.body.appendChild(container)
container.appendChild(article)
article.appendChild(h1Tag)
article.appendChild(pTag)