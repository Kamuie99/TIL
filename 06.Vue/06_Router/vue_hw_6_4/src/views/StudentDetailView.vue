<template>
  <div>
    <h2>학생 상세 정보 페이지입니다.</h2>
    <p>이름: {{ studentName }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const studentName = ref('');
studentName.value = router.currentRoute.value.params.name;

</script>