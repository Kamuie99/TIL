<template>
    <div class="create-outer">
      <form @submit.prevent="createQuiz" class="quiz-create-container">
        <h2>퀴즈 생성</h2>
        <label for="problem">문제</label>
        <textarea id="problem" v-model="problem" @input="checkWriting"></textarea>
        <label for="answer">답안</label>
        <input type="text" id="answer" v-model="answer" @input="checkWriting">
        <button type="submit" class="create-button">퀴즈 생성</button>
      </form>
    </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';

const problem = ref('');
const answer = ref('');
const emit = defineEmits(['createQuiz', 'writingCheck']);
const createQuiz = function() {
  const newQuiz = {
    pk : 0,
    question : problem.value,
    answer : answer.value,
  }
  problem.value = ''
  answer.value = ''
  emit('createQuiz', newQuiz)
}

const checkWriting = () => {
  emit('writingCheck', problem.value !== '' || answer.value !== '');
}

</script>


<style scoped>
.create-outer {
  display: flex;
  justify-content: center;

  width: 100%;
}

.quiz-create-container {
  display: flex;
  flex-direction: column;

  width: 83%;
  margin-bottom: 20px;
  padding: 30px 20px;

  border: 1px solid lightgray;
  background-color: #F5F5F5;

  border-radius: 10px;
}

.quiz-create-container h2 {
  margin: 0;
  margin-bottom: 20px;
}

.quiz-create-container label {
  margin-top: 10px;
  margin-bottom: 10px;
}

#problem {
  height: 60px;
  resize: none;

  border: 1px solid lightgray;
  border-radius: 5px;

  padding-top: 10px;
}
#answer {
  height: 30px;

  border: 1px solid lightgray;
  border-radius: 5px;
}
.create-button {
  margin-top: 20px;
  height: 35px;
  
  background-color: #007BFF;
  color: white;
  
  border: 1px solid lightgray;
  border-radius: 5px;
}
</style>