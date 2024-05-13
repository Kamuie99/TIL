<template>
  <div>
    <h1>학생 상세 정보 목록입니다.</h1>
    <RouterLink 
      v-for="student in students" 
      :key="student" 
      :to="{ name: 'StudentDetailView', params:{ name: student.name }}"
      class="RouterLink"
    >
      <p>{{ student.name }} 학생 정보 보기</p>
    </RouterLink>
  </div>
</template>
<script setup>
const students = [
  { name : '김하나'},
  { name : '김두리'},
  { name : '김서이'},
]
</script>
<style scoped>
.RouterLink {
  text-decoration: none;
  color: black;
}
</style>