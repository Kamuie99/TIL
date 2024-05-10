<template>
    <div class="search-container">
      <input v-model="searchQuery" type="text" placeholder="영화 제목을 검색해보세요" @keyup.enter="fetchYoutubeVideos">
      <button @click="fetchYoutubeVideos">검색</button>
    </div>
    <div class="search-cards">
      <YoutubeCard
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @click="openModal(video)"
      />
    </div>
    <YoutubeReviewModal 
      v-if="showModal" 
      :video-id="selectedVideoId" 
      :video-title="selectedVideoTitle" 
      @close="showModal = false"
    />
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import YoutubeCard from '@/components/YoutubeCard.vue'
import YoutubeReviewModal from '@/components/YoutubeReviewModal.vue';

const searchQuery = ref('')
const videos = ref([])
const showModal = ref(false)
const selectedVideoId = ref(null)
const selectedVideoTitle = ref('')

const fetchYoutubeVideos = async () => {
  const apiKey = ''; // 이곳에 api key를 입력하시오.
  const searchUrl = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(searchQuery.value + " review")}&type=video&key=${apiKey}`;
  const response = await axios.get(searchUrl);
  videos.value = response.data.items;
}

const openModal = (video) => {
  selectedVideoId.value = video.id.videoId
  selectedVideoTitle.value = video.snippet.title
  showModal.value = true;
};
</script>

<style scoped>
.search-container {
  height: 100px;
  
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.search-container input {
  width: 40%;
  height: 40px;
  border: 1px solid lightgray;
  border-radius: 5px;
  padding: 5px;
}
.search-container button {
  margin-left: 10px;
  width: 5%;
  height: 52px;
  border: none;
  border-radius: 5px;
  background-color: #3297CE;
  color: white;
  cursor: pointer;
}

.search-cards {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>