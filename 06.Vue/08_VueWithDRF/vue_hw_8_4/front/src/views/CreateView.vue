<template>
    <div>
      <h1>게시글 작성</h1>
      <form @submit.prevent="createArticle">
        <label for="title">제목 : </label>
        <input type="text" name="title" v-model.trim="title">
        <label for="content">내용 : </label>
        <input type="text" name="content" v-model.trim="content">
        <input type="submit" value="create">
      </form>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router'

const store = useArticleStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then((res) => {
      console.log(res)
      router.push({ name: 'home'})
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>