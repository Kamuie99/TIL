<template>
  <header class="header">
    <nav class="header-nav">
      <RouterLink :to="{name: 'home'}">Home</RouterLink>
      <span>|</span>
      <RouterLink :to="{name: 'products'}">Products</RouterLink>
      <span>|</span>
      <span class="last-one">
        <RouterLink :to="{name: 'favorite'}">Favorite</RouterLink>
        <span class="likes" v-if="store.favoriteProduct.length > 0">{{ store.favoriteProduct.length }}</span>
        <span class="dislikes" v-else> </span>
      </span>

    </nav>
  </header>
  <main class="main">
    <RouterView />
  </main>
  <footer></footer>
</template>

<script setup>
import { useProductStore } from '@/stores/products';
const store = useProductStore()

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
.header-nav a {
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

.likes {
  display: inline-block;
  width: 20px;
  height: 20px;
  margin-left: 5px;
  background-color: red;
  border-radius: 50%;
  text-align: center;

  font-size: 15px;
}

.dislikes {
  display: inline-block;
  width: 20px;
  height: 20px;
  margin-left: 5px;
  text-align: center;
}

.last-one {
  display: flex;
  align-items: center;
}

</style>