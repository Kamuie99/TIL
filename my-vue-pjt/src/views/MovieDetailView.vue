<template>
  <div v-if="movie" class="movie-detail-container">
    <img :src="movieImgUrl" alt="Movie Poster" class="poster">
    <div class="movie-title-container">
      <p class="tiny-title">{{ movie.title }}</p>
      <div class="tiny-about">
        <p><span>개봉일:</span> {{ movie.release_date }}</p>
        <p><span>러닝타임:</span> {{ movie.runtime }} 분</p>
        <p><span>TMDB 평점:</span> {{ movie.vote_average }}</p>
      </div>
    </div>
    <div>
      <p class="tiny-title">장르</p>
      <div class="genres">
        <p v-for="genre in movie.genres" :key="genre.id">
          {{ genre.name }}
        </p>
      </div>
    </div>
    <div class="movie-about-container">
      <p class="tiny-title">줄거리</p>
      <p class="overview">{{ movie.overview }}</p>
    </div>
    <div class="youtube-container">
      <p class="tiny-title">공식 예고편</p>
      <img src="@/assets/images.png" alt="Watch Trailer" class="youtube-link" @click="openYoutubeTrailer(movie.title)">
    </div>
    <YoutubeTrailerModal v-if="showModal" :video-id="videoId" @close="showModal = false" />
  </div>
</template>
<script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  import YoutubeTrailerModal from '@/components/YoutubeTrailerModal.vue';

  const movie = ref(null);
  const route = useRoute();
  const showModal = ref(false);
  const videoId = ref(null);

  const apiKey = 'de629d7c668f8707dcdae72aed5f5a68'
  const fetchMovieDetail = async () => {
    const movieId = route.params.movieId;
    const url = `https://api.themoviedb.org/3/movie/${movieId}?api_key=${apiKey}&language=ko-KR`;
    try {
      const response = await axios.get(url);
      movie.value = response.data;
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const movieImgUrl = computed(() => {
    return movie.value ? `https://image.tmdb.org/t/p/w500${movie.value.poster_path}` : '';
  });

  onMounted(fetchMovieDetail)

  const youtubeApiKey = 'AIzaSyB_Zf08-aQ-jFs-vPGT7gGOnp_KDWkp3Bc';

  const fetchYoutubeTrailer = async (movieTitle) => {
    const searchUrl = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(movieTitle)} official trailer&type=video&key=${youtubeApiKey}`;
    try {
      const response = await axios.get(searchUrl);
      if (response.data.items.length > 0) {
        videoId.value = response.data.items[0].id.videoId;
        showModal.value = true;
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const openYoutubeTrailer = async (title) => {
    await fetchYoutubeTrailer(title);
  }



</script>
<style scoped>
.movie-detail-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.poster {
  width: 300px;
  height: 450px;
}

.movie-about-container {
  width: 90%;
  text-align: center;
}
.overview {
  margin-top: 10px;
  margin-bottom: 30px;
}
.movie-title-container {
  margin-top: 20px;
  text-align: center;
}
.movie-title-container span {
  font-weight: bold;
}

.tiny-title {
  text-align: center;
  font-weight: bold;
  font-size: 19px;
}
.tiny-about {
  margin-top: 30px;
  margin-bottom: 30px;
}
.tiny-about p {
  margin: 10px
}
.genres {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  margin-bottom: 30px;
}
.genres > p {
  margin-left: 10px;
  margin-right: 10px;
}
.youtube-link {
  width: 40px;
  height: 20px; /* 적절한 크기 설정 */
  margin-top: 10px;
  margin-bottom: 30px;
  cursor: pointer; /* 마우스 오버 시 포인터 변경 */
  height: auto; /* 비율 유지 */
  margin-top: 10px;
  margin-bottom: 30px;
  transition: transform 0.3s; /* 부드러운 변형을 위한 트랜지션 추가 */
}

.youtube-link:hover {
  transform: scale(1.1); /* 호버 시 아이콘이 약간 확대 */
}
.youtube-container {
  text-align: center;
}
</style>