<template>
  <li>
    {{ myProp.name }} - {{ myProp.price }}원
  </li>
</template>
<script setup>
defineProps({
  myProp: Object
})
</script>