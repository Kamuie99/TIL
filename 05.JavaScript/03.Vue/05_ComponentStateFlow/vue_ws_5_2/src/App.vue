<template>
  <header class="header">
    <div class="title_box">
      <p>명함 관리 페이지</p>
    </div>
  </header>
  <main class="main">
    <div class="explain">
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </div>
  </main>
  <h3>보유 명함 목록</h3>
  <article class="article">
    <BusinessCard/>
  </article>
  <footer class="footer">
    <p>© 2023 My Business Cards</p>
  </footer>
</template>
<script setup>
import BusinessCard from '@/components/BusinessCard.vue';

</script>