<template>
  <div>
    <h1>업데이트</h1>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="store.updateBalance(balance.name)">+</button>
  </div>
</template>
<script setup>
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance';

const route = useRoute()
const store = useBalanceStore()

const name = route.params.name
const balance = store.getBalanceByName(name)


</script>