<template>
  <div class="child-component">
    <h2>자식 페이지</h2>
    <p>{{ children.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  children: Object
})
</script>

<style scoped>
.child-component {
  border: 1px solid lightgray;
  background-color: white;

  margin-bottom: 10px;
}
</style>