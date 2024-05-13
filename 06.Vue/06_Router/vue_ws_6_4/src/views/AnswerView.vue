<template>
    <div class="answer-container">
      <h3>{{ problemId }}번 문제</h3>
      <h1>정답 확인</h1>
      <div class="answer-inner">
        <p :style="{ color: isCorrectColor }" class="bold">{{ isCorrect }}</p>
        <p :style="{ color: isCorrectColor }">나의 제출 답안: {{ userAnswer }}</p>
        <p>정답: {{ correctAnswer }}</p>
      </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router';

const route = useRoute();

const problemId = ref(route.params.pk);
const correctAnswer = ref(route.params.answer);
const userAnswer = ref(route.query.userAnswer); 

const isCorrect = computed(() => {
  return userAnswer.value === correctAnswer.value ? '정답입니다!' : '오답입니다!';
});

const isCorrectColor = computed(() => {
  return isCorrect.value === '정답입니다!' ? 'green' : 'red';
});

</script>

<style scoped>
.answer-container {
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid lightgray;
  border-radius: 10px;
  background-color: #F5F5F5;
}

.answer-container h1 {
  margin: 0;
}

.answer-container h3 {
  margin-bottom: 0;
}

.answer-inner {
  width: 90%;
  height: 150px;
  margin-top: 20px;
  border: 1px solid lightgray;
  border-radius: 10px;
  background-color: white;

  padding: 10px;
}

.bold {
  font-weight: bolder;
}
</style>