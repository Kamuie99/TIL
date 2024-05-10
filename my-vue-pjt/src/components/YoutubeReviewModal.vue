<template>
  <div class="modal" @click.self="$emit('close')">
    <div class="modal-inner">
      <div class="title-button">
        <p class="title">{{ videoTitle }}</p>
        <button @click="$emit('close')">x</button>
      </div>
      <iframe
        width="560"
        height="315"
        :src="youtubeUrl"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<script setup>
import { computed, defineProps } from 'vue';

const props = defineProps({
  videoId: String,
  videoTitle: String,
});

const youtubeUrl = computed(() => {
  return `https://www.youtube.com/embed/${props.videoId}?autoplay=1`;
});
</script>

<style scoped>
.modal {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.8);
}
.modal-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 38rem;

  background-color: white;
  padding: 10px;
}

button {
  cursor: pointer;
  background-color: white;
  border: none;
  font-size: 20px;

  align-self: flex-end;
}
.title-button {
  width: 36rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding-left: 20px;
  padding-right: 20px;
  margin-bottom: 30px;
  align-items: center;
}

.title {
  font-weight: bold;
}
iframe {
  margin-bottom: 20px;
}
</style>