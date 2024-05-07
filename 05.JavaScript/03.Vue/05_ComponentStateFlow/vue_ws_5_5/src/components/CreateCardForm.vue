<template>
  <form @submit.prevent="createCardFunc">
    <label for="name-input">이름</label>
    <input type="text" v-model="name" id="name-input" />
    <label for="title-input">직함</label>
    <input type="text" v-model="title" id="title-input" />
    <button type="submit">명함 추가</button>
  </form>
</template>

<script setup>
import { ref, defineEmits } from 'vue'

const name = ref('')
const title = ref('')
const emit = defineEmits(['createCardEvent'])

function createCardFunc() {
  if (name.value.trim() && title.value.trim()) {
    emit('createCardEvent', { name: name.value, title: title.value })
    name.value = ''
    title.value = ''
  }
}
</script>

<style scoped>
form {
  display: flex;
  justify-content: center;
  align-items: center;
}

form label {
  margin-left: 20px;  
  margin-right: 10px;

  font-weight: bold;
}

input {
  border: 1.5px solid #7AB9E4;
  border-radius: 5px;
  width: 200px;
  height: 30px;
}

button {
  margin-left: 10px;
  background-color: white;
  color: #7AB9E4;
  font-weight: bold;
  border: 1.5px solid #7AB9E4;
  border-radius: 5px;

  height: 35px;
}
</style>
