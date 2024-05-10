<template>
  <div class="movies-container-outer">
    <div class="movies-container">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div>
  </div>
</template>

<script setup>
import  axios from 'axios'
import { ref, onMounted } from 'vue'
import MovieCard from '@/components/MovieCard.vue'

const apiKey = 'de629d7c668f8707dcdae72aed5f5a68';
const movies = ref([]);

const fetchTopRatedMovies = async () => {
  try {
    const url = `https://api.themoviedb.org/3/movie/top_rated?api_key=${apiKey}&language=ko-KR&page=1`;
    const response = await axios.get(url)
    movies.value = response.data.results;
  } catch (error) {
    console.error('Error: ', error)
  }
}

onMounted(fetchTopRatedMovies);

</script>

<style scoped>
.movies-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap: wrap;
  width: 90%;
}

.movies-container-outer {
  display: flex;
  justify-content: center;
}
</style>