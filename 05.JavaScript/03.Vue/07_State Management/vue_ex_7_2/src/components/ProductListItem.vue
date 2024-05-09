<template>
  <li>
    {{ product.id }} - {{ product.title }} - {{ product.body }}  
    <button @click="store.deleteProduct(product.id)">Delete</button>
  </li>
</template>
<script setup>
import { useProductStore } from '@/stores/product'

const store = useProductStore()

defineProps({
  product: Object
})
</script>