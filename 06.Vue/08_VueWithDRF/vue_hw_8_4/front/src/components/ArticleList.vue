<template>
  <div>
    <button @click="goToCreateView">게시글 생성</button>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
import ArticleListItem from './ArticleListItem.vue';
import router from '../router';

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

const goToCreateView = () => {
  router.push({ name: 'CreateView' })
}
</script>

<style lang="scss" scoped>

</style>