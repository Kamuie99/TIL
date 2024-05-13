<template>
  <div>
    <h1>User Profile</h1>
    <p>Username: {{ username }}</p>
  </div>
</template>
<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();
const username = router.currentRoute.value.params.username;
</script>