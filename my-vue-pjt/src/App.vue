<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <span>
        <RouterLink to="/">
          <img src="@/assets/ssafy_logo.png" alt="logo" class="logo">
        </RouterLink>
      </span>
      <span class="links">
        <RouterLink to="/movies" active-class="active">영화조회</RouterLink>
        <RouterLink to="/review-search" active-class="active">리뷰검색</RouterLink>
      </span>
    </nav>
  </header>
  <main>
    <div></div>
  </main>
  <RouterView />
</template>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 10px;
  height: 40px;
  margin-bottom: 20px;
  background-color: #C9D6DC;
}

a {
  text-decoration: none;
  color: black;
}

.links > a {
  margin-right: 20px;
}

.logo {
  margin-left: 10px;
  width: 40px;
  height: 30px;
}

.active {
  color: green;
}
</style>
