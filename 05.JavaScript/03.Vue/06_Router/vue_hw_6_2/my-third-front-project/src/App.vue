<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from './components/MainPage.vue';

</script>

<template>
  <header>
    <MainPage/>
    <nav>
      <RouterLink to="/">Some</RouterLink>
      <RouterLink to="/other">Other</RouterLink>
    </nav>
  </header>

  <RouterView/>
</template>

<style scoped>
</style>
