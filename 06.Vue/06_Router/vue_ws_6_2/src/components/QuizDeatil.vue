<template>
    <div v-for="quiz in quizData" :key="quiz.pk" class="quiz-inner">
      <h4>{{ quiz.pk }}번 문제. {{ quiz.question }}</h4>
      <p>정답 입력</p>
      <input :id="quiz.pk" type="text">
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  quizData: {
    type: Array
  }
})
</script>

<style scoped>
.quiz-inner {
  background-color: #F9F9F9;
  border: 1px solid lightgray;
  border-radius: 10px;
  width: 100%;
  height: 170px;
  padding-left: 20px;

  margin-bottom: 15px;
}

.quiz-inner input {
  width: 95%;
  height: 30px;
  border: 1px solid lightgray;
  border-radius: 5px;
}
</style>