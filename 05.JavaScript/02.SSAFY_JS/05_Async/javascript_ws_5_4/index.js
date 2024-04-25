/* 
아래에 코드를 작성해주세요.
*/
const API_KEY = 'bb10ae5537462edeb09ce3a78a4c96ac'
const API_URL = 'https://ws.audioscrobbler.com/2.0/'

const keyword = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box__button')

searchBtn.addEventListener('click', function fetchAlbums(page = 1, limit = 10) {
  axios({
    method: 'get',
    url: API_URL,
    params: {
      method: 'album.search',
      album: keyword.value,
      api_key: API_KEY,
      format: 'json',
      page,
      limit,
    }
  })
    .then((response) => {
      const search_resultDiv = document.querySelector('.search-result')
      search_resultDiv.innerHTML = ''

      const albums = response.data.results.albummatches.album

      albums.forEach(album => {
        const h2Tag = document.createElement('h2')
        const pTag = document.createElement('p')
        const innerDiv = document.createElement('div')
        const imgTag = document.createElement('img')
        const outDiv = document.createElement('div')


        h2Tag.textContent = album.artist
        pTag.textContent = album.name
        imgTag.src = album.image[1]['#text']
        innerDiv.classList.add('search-result__text')
        outDiv.classList.add('search-result__card')

        innerDiv.appendChild(h2Tag)
        innerDiv.appendChild(pTag)
        outDiv.appendChild(imgTag)
        outDiv.appendChild(innerDiv)

        search_resultDiv.appendChild(outDiv)
      });

    })
    .catch((error) => {
      alert('잠시 후 다시 시도해주세요')
    })
})


