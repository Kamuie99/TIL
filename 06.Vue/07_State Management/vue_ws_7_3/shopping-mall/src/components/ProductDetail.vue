<template>
    <div class="product-container">
      <h3>{{ product.name }}</h3>
      <img :src=product.imagePath alt="">
      <p>₩ {{ product.price }}</p>
      <button 
        id="heart" 
        :class="{ 'color-heart' : product.isFavorite}"
        @click="toggleFavorite(product.name)"
      >♡</button>
    </div>
</template>

<script setup>
import { useProductStore } from '@/stores/products';
const store = useProductStore()


defineProps({
  product: Object
})

const toggleFavorite = (productName) => {
  store.toggleFavorite(productName)
}

</script>

<style scoped>
.product-container {
  width: 300px;
  height: 400px;

  text-align: center;
  border: 1px solid lightgray;
  margin: 15px;
}

.product-container > img {
  width: 250px;
  height: 150px;
}

.color-heart {
  color: red;
}

#heart {
  font-size: 20px;
  background-color: white;
  border: none;
}



</style>