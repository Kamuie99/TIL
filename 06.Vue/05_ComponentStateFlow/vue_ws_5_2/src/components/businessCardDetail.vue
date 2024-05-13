<template>
  <div v-for="person in people" :key="person.name">
    <span>이름 : {{ person.name }}</span>
    <p>직함 : {{ person.title }}</p>
  </div>
</template>
<script setup>
defineProps({
  people: Array,
})
</script>