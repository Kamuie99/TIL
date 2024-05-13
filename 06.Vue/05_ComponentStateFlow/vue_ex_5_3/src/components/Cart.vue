<template>
  <ul>
    <li v-for="product in products">
      {{ product.name }} - {{ product.price }}원
      <button @click="deleteProduct(product)">삭제</button>
    </li>
  </ul>
</template>
<script setup>
defineProps({
  products: Array
})

const emit = defineEmits(['delete-item'])

const deleteProduct = (product) => {
  emit('delete-item', product);
}
</script>