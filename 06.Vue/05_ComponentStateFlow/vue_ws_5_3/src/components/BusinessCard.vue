<template>
  <businessCardDeatil :people="businessCards" @delete-card="deletePerson"/>
</template>
<script setup>
import businessCardDeatil from '@/components/businessCardDetail.vue';
import { ref } from 'vue'


const businessCards = ref([
  {name: '일론 머스크', title: '테슬라 테크노킹'},
  {name: '래리 엘리슨', title : '오라클 창업주'},
  {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
  {name: '래리 페이지', title: '구글 공동창업주'},
  {name: '세르게이 브린', title: '구글 공동창업주'}
])

const deletePerson = (person) => {
  const index = businessCards.value.indexOf(person)
  if (index !== -1) {
    businessCards.value.splice(index, 1)[0]
  }
}
</script>