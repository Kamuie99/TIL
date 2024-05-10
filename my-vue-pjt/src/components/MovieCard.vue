<template>

    <RouterLink :to="`${movie.id}`" class="moive-card-container">
      <img :src="movieImgUrl" alt="moviePoster">
      <div class="movie-about-container">
        <p class="movie-title">{{ movie.title }}</p>
        <p class="movie-overview">{{ movie.overview }}</p>
      </div>
  </RouterLink>
</template>

<script setup>
import { computed, defineProps } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps({
  movie: Object
})

const movieImgUrl = computed (() => {
  return `https://image.tmdb.org/t/p/w500${props.movie.poster_path}`
});
  
</script>

<style scoped>
.moive-card-container {
  display: flex;
  flex-direction: column;
  width: 300px;
  border: 0.5px solid lightgray;
  margin: 10px;
}
.moive-card-container > img {
  width: 300px;
  height: 450px;
}
.movie-about-container {
  padding: 13px;
}
.movie-title {
  font-weight: bold;
  margin-bottom: 10px;
  font-size: 1rem;
}
.movie-overview {
  font-size: 14px;
}

a {
  text-decoration: none;
  color: black;
}
</style>