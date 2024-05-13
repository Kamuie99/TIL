<template>
  <header>
    <div class="quiz-app">
      <div class="title-explain">
        <div class="app-header">
          <p class="app-name">Quiz 퀴즈</p>
        </div>
        <div class="app-description">
          <p class="app-explain">{{ explainGame }}</p>
        </div>
      </div>
      <nav class="app-nav">
        <div class="nav-inner">
          <RouterLink to="/" class="nav-link">Home</RouterLink> | 
          <RouterLink to="/quiz" class="nav-link">Quiz</RouterLink> |
        </div>
      </nav>
    </div>
  </header>
  <main>
    <div class="main-container">
      <RouterView />
    </div>
  </main>
  <footer>
  </footer>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { ref } from 'vue';

const explainGame = ref('여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!')

</script>

<style scoped>

header {
  width: 100%;
  height: 300px;

  display: flex;
  justify-content: center;
  align-items: center;
}

main {
  width: 100%;
  height: 1100px;

  display: flex;
  justify-content: center;
  align-items: center;
}

.quiz-app {
  width: 50%;
  height: 90%;
  border: 1px solid #F5F5F5;
  background-color: #F5F5F5;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title-explain {
  width: 90%;
  height: 70%;
  border: 1px solid gray;
  border-radius: 10px;
}

.app-header {
  background-color: #FF922B;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  height: 40%;

  display: flex;
  justify-content: center;
  align-items: center;
}

.app-description {
  background-color: white;
  height: 60%;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;

  display: flex;
  justify-content: center;
  align-items: center;
}

.app-name {
  margin: 0;
  font-size: 27px;
  font-weight: bold;
  color: white;
}
.app-explain {
  margin: 0;
}

.app-nav {
  margin-top: 20px;
  width: 90%;
  height: 30px;


  text-decoration: none;
  background-color: #333333;
  color: white;

  display: flex;
  justify-content: center;
  align-items: center;
}

.app-nav a {
  color: white;
}

.nav-inner {
  width: 30%;
  display: flex;
  justify-content: space-around;
}

.main-container {
  width: 70%;
}
</style>
