<template>
  <header class="header">
    <div class="title_box">
      <p>명함 관리 페이지</p>
    </div>
  </header>
  <main class="main">
    <div class="explain">
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </div>
    <CreateCardForm @createCardEvent="addPerson" />
  </main>
  <h3>보유 명함 목록</h3>
  <article class="article">
    <BusinessCard :people="businessCards" @delete-card="deletePerson" />
  </article>
  <footer class="footer">
    <p>© 2023 My Business Cards</p>
  </footer>
</template>

<script setup>
import BusinessCard from '@/components/BusinessCard.vue'
import CreateCardForm from '@/components/CreateCardForm.vue'
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

const addPerson = (cardInfo) => {
  businessCards.value.push(cardInfo)
}
</script>
