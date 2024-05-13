<template>
    <div>
      <h1>{{ username }}이 작성한 게시글</h1>
      <RouterLink v-for="post in posts" :key="post.id" :to="{ name:'post-detail', params: { id: post.id }}">
        <PostListItem :post="post"/>
      </RouterLink>
    </div>
    <hr>
    <RouterView/>

</template>

<script setup>
import { defineProps } from 'vue'
import { RouterLink, RouterView } from 'vue-router';
import PostListItem from '@/components/PostListItem.vue'

const props = defineProps(['username'])


import { ref } from 'vue'
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
</script>

<style scoped>

</style>