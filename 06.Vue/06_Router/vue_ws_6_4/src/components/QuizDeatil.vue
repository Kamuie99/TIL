<template>
    <div v-for="quiz in quizData" :key="quiz.pk" class="quiz-inner">
      <h4>{{ quiz.pk }}번 문제. {{ quiz.question }}</h4>
      <p>정답 입력</p>
      <input v-model="answers[quiz.pk]" :id="quiz.pk" type="text" @keyup.enter="submitAnswer(quiz)">
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';


const answers = ref({});
const router = useRouter();

const props = defineProps({
  quizData: {
    type: Array
  }
})

const submitAnswer = (quiz) => {
  const answer = answers.value[quiz.pk]
  router.push({ 
    name: 'AnswerView',
    params: { pk: quiz.pk, answer: quiz.answer },
    query: { userAnswer: answer }
  });
};
</script>

<style scoped>
.quiz-inner {
  background-color: #F9F9F9;
  border: 1px solid lightgray;
  border-radius: 10px;
  width: calc(100% - 40px);
  height: 180px;
  padding-left: 20px;
  padding-right: 20px;
  margin-bottom: 15px;
}

.quiz-inner input {
  width: 95%;
  height: 30px;
  border: 1px solid lightgray;
  border-radius: 5px;
}
</style>