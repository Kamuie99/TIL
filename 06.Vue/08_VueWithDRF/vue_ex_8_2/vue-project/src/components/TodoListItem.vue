<template>
    <div>
      <p>{{ todo.work }}</p>
      <p>{{ todo.content }}</p>
      <p>{{ todo.is_completed }}</p>
      <p>{{ todo.created_at }}</p>
      <hr>
    </div>
</template>

<script setup>
defineProps({
  todo: Object
})
</script>

<style scoped>

</style>