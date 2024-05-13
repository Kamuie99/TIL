<template>
  <div>
    <h1>장바구니 페이지</h1>
    <div class="products-conatiner">
        <ProductDetail 
          v-for="product in store.favoriteProduct"
          :key="product.name"
          :product="product"/>
      </div>
  </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue';
import { useProductStore } from '@/stores/products';
const store = useProductStore()
</script>

<style scoped>
.products-conatiner {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  flex-wrap: wrap;
}
</style>