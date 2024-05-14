<template>
  <main>
    <div class="main-container _2">
      <BoxOffice/>
    </div>
    <div class="main-container _1">

    </div>
    <div class="main-container-big _2">

    </div>
  </main>
</template>

<script setup>
import BoxOffice from '@/components/BoxOffice.vue';


</script>

<style scoped>
* {
  color: rgb(165, 165, 165);
}
.main-container {
  height: 46vh;
}
.main-container-big {
  height: 92vh;
  background-color: #1b1b1b;
}
._1 {
  background-color: #1b1b1b;
}
._2 {
  background-color: #E5DFCC;
}
</style>
