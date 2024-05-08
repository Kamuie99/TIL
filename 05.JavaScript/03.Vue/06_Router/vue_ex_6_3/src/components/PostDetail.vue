<template>
  <div>
    <p>번호 : {{ route.params.id }}</p>
    <p>제목 : {{ selectedPost.title }}</p>
    <p>내용 : {{ selectedPost.content }}</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const posts = ref([
  {
    id: 1,
    title: 'Post 1',
    content: 'Content 1'
  },
  {
    id: 2,
    title: 'Post 2',
    content: 'Content 2'
  },
  {
    id: 3,
    title: 'Post 3',
    content: 'Content 3'
  }
])

const selectedPost = computed(() => {
  const postId = Number(route.params.id);
  return posts.value.find(post => post.id === postId);
});


</script>

<style scoped>

</style>