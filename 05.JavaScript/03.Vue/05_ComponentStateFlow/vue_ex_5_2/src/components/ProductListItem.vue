<template>
  <div>
    <a>
      {{ product.name }} - {{ product.price }}원
    </a>
    <button>장바구니에 추가</button>
  </div>
</template>
<script setup>
defineProps({
  product: Object
})
</script>