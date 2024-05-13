<template>
  <div class="quiz-app">
    <div class="app-header">
      <!-- 앱 이름-->
    </div>
    <div class="app-description">
      <!-- 앱 설명 -->
    </div>
    <nav class="app-nav">
      <RouterLink to="/" class="nav-link">Home</RouterLink>
    </nav>
  </div>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
</style>
