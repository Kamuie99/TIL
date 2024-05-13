<template>
  <p>현재 보유중인 명함 수: {{ people.length }}</p>
  <div class="cards">
    <div v-for="person in people" :key="person.name" class="article_card">
      <span>이름 : {{ person.name }}</span>
      <p>직함 : {{ person.title }}</p>
      <button @click="deletePerson(person)">명함 삭제</button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  people: Array,
})

const emit = defineEmits(['delete-card'])

const deletePerson = (person) => {
  emit('delete-card', person)
}
</script>
