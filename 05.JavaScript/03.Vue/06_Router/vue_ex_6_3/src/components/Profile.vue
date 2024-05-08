<template>
  <div>
    <h1>상세 프로필</h1>
    <p>반갑습니다. {{ username }}입니다.</p>
  </div>
</template>
<script setup>
import { defineProps } from 'vue'

const props = defineProps(['username'])
</script>