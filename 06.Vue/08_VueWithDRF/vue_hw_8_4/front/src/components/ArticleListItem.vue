<template>
    <div v-if="article">
      <h3>{{ article.id }}번 게시글</h3>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <hr>
    </div>
</template>

<script setup>
defineProps({
  article: Object
})
</script>

<style scoped>

</style>