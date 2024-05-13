<template>
  <div class="card">
    <h1>가수 이름</h1>
    <img src="@/assets/singer.jpg">
    <p>가수 소개글</p>
    <div class="albums">
      <SingerAlbum />
      <SingerAlbum />
    </div>
  </div>
</template>
<script setup>
import SingerAlbum from '@/components/singers/SingerAlbum.vue'
</script>
<style scoped>
img {
  border-radius: 50%;
  width: 200px;
}

.card {
  text-align: center;
}

.albums {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
</style>