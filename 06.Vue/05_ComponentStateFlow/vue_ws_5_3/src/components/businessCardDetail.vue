<template>
  <div v-for="person in people" :key="person.name">
    <span>이름 : {{ person.name }}</span>
    <p>직함 : {{ person.title }}</p>
    <button @click="deletePerson(person)">명함 삭제</button>
  </div>
</template>
<script setup>
defineProps({
  people: Array,
})

const emit = defineEmits(['delete-card'])

const deletePerson = (person) => {
  emit('delete-card', person)
}
</script>