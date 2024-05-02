<template>
  <div class="list">
    <h1>가수 목록</h1>
    <SingerDetail v-for="singer in singers" :key="singer.name">
    </SingerDetail>
  </div>
</template>
<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue'

const singers = [
  { name: 'adele' }, { name: 'maroon 5' }, { name: 'Dua Lipa' }
]

</script>
<style scoped>
.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
  border: 1px solid gray;
}

.list {
  text-align: center;
}

h1 {
  color: orangered;
}
</style>
<style>
/* h1 {
  color: green;
} */
</style>