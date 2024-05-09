<template>
  <div class="parent-component">
    <h1>부모 컴포넌트</h1>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage
    v-for="children in family.children"
    :key="children"
    :children="children"/>
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';

defineProps({
  family: Object
})

</script>

<style scoped>
.parent-component {
  border: 1px solid lightgray;
  background-color: #F9F9F9;

  margin-bottom: 20px;
  padding: 20px;

  text-align: center;
}
</style>