<template>
  <div class="card-contents">
    <img :src="video.snippet.thumbnails.medium.url" alt="Thumbnail">
    <div class="card-about">
      <h3 class="card-title">{{ video.snippet.title }}</h3>
      <p>{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  video: Object
});
</script>

<style scoped>
.card-contents {
  width: 90%;
  display: flex;
  border: 1px solid lightgray;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 20px;
  cursor: pointer;
}
.card-title {
  font-weight: bold;
  font-size: x-large;
  margin-bottom: 30px;
}
.card-about {
  margin-left: 20px;
}
</style>