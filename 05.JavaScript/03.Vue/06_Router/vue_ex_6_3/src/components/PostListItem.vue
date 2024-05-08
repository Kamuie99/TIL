<template>
    <div>
      {{ post.id }}.
      제목: {{ post.title }}
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  post: {
    type: Object
  }
})
</script>

<style scoped>

</style>