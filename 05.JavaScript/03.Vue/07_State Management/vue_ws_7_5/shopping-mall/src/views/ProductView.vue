<template>
    <div>
      <h1>상품 목록 페이지</h1>
      <div class="products-conatiner">
        <ProductDetail 
          v-for="product in store.productList"
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