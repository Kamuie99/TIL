<template>
  <header class="header">
    <nav class="header-nav">
      <RouterLink :to="{name: 'home'}">Home</RouterLink>
      <span>|</span>
      <RouterLink :to="{name: 'products'}">Products</RouterLink>
      <span>|</span>
      <RouterLink :to="{name: 'favorite'}">Favorite</RouterLink>
    </nav>
  </header>
  <main class="main">
    <RouterView />
  </main>
  <footer></footer>
</template>

<script setup>
</script>

<style scoped>
.header {
  width: 100%;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;

  background-color: #333333;
  color: white;
}
.header-nav > a {
  color: white;
  text-decoration: none;
}
.header-nav {
  width: 30%;

  display: flex;
  justify-content: space-around;
}
.main {
  padding: 20px;
}

</style>