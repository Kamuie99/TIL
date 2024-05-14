<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header class="header">
    <nav class="header-nav">
      <div class="nav-item nav-bar">
        <RouterLink to="/foryou">For You</RouterLink>
        <RouterLink to="">Movies</RouterLink>
        <RouterLink to="">Community</RouterLink>
        <RouterLink to="">Nearby</RouterLink>
      </div>
      <div class="nav-item">
        <RouterLink to="/">
          <img src="" alt="로고이미지">
        </RouterLink>
      </div>
      <div class="nav-item">
        <p>검색</p>
      </div>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
.header {
  position: sticky; /* 상단 고정 */
  top: 0; /* 화면 맨 위에 위치 */
  z-index: 1000;
  width: 100%;
  display: flex;
  align-items: center;
  height: 8vh;
  background-color: #1b1b1b;
  border-bottom: 1px solid #2f2f2f;
}
.header-nav {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.nav-item {
  width: 500px;
  text-align: center;
}
.nav-bar {
  display: flex;
  justify-content: space-around;
}
.nav-bar > a {
  text-decoration: none;
  color: rgb(165, 165, 165);
}
</style>