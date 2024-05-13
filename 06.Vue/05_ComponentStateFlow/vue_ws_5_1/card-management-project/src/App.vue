<template>
  <header class="header">
    <div class="title_box">
      <p>명함 관리 페이지</p>
    </div>
  </header>
  <main class="main">
    <div class="explain">
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </div>
  </main>
  <article></article>
  <footer class="footer">
    <p>© 2023 My Business Cards</p>
  </footer>
</template>
<script setup>
</script>
<style>
.header {
  width: 100%;
  height: 20vh;

  display: flex;
  justify-content: center;
  align-items: center;
}

.title_box {
  width: 300px;
  height: 100px;
  
  text-align: center;
  font-weight: bold;
  font-size: 30px;
  
  background-color: #007ACC;
  color: white;
}

.main {
  width: 100%;
  height: 60vh;
}

.explain {
  text-align: center;
}

.footer {
  width: 100%;
  height: 10vh;

  display: flex;
  justify-content: center;
  align-items: center;
  
  background-color: #F0F0F0;

  position: fixed;
  bottom: 0;
}
</style>