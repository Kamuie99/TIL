<template>
  <div class="recommendMovie-container">
    <div class="title-area">
      <span class="RecommendMovieTitle">닉네임 님을 위한 시추</span>
      <button>다시 찾아보기</button>
    </div>
    <div class="wrapper">
      <div class="carousel-container">
        <carousel :autoplay="3000" :wrap-around="true">
          <slide v-for="slide in slides" :key="slide" class="hi">
            <div class="slide-inner">
              <div class="slide-title">
                <p class="wrapper_title">영화 제목 {{ slide }}</p>
                <p class="wrapper_date">2024.05.14</p>
              </div>
              <div class="carousel__item">
                <img :src="slide" class="slideImg1">
              </div>
            </div>
          </slide>
      
          <template #addons>
            <navigation />
            <pagination />
          </template>
        </carousel>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineComponent, ref } from 'vue';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import "vue3-carousel/dist/carousel.css";
import img_1 from '@/assets/mov1.jpg'
import img_2 from '@/assets/mov2.jpg'
import img_3 from '@/assets/mov3.jpg'
import img_4 from '@/assets/mov4.jpg'

const slides = ref([img_1, img_2, img_3, img_4])

defineComponent({
  name: 'Autoplay',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
});
</script>

<style>
.slide-title {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  align-items: center;
  color: rgb(165, 165, 165);
  align-self: flex-start;
  margin-bottom: 30px;
  font-size: 20px;
  width: 100%;
}
.tiny-title {
  align-self: flex-end;
  margin-left: 20px;
}
.recommendMovie-container{
  height: 92vh;
}
.title-area{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: 40px;
  margin-right: 40px;
  height: 12vh;
}
.title-area > span {
  font-size: 20px;
}
.RecommendMovieTitle {
  font-size: 17px;
  color: black;
  
}
.wrapper {
  height: 80vh;
  display: flex;
  flex-direction: column;
  justify-content: center;

  align-items: center;
  background-color: #1b1b1b;
  border-top-right-radius: 40px;
  border-top-left-radius: 40px;
}
.wrapper_title{
  color: rgb(165, 165, 165);
  align-self: flex-start;
  margin-left: 30px;
  font-size: 20px;
}
.wrapper_date {
  margin-right: 20px;
}
.slide-inner {
  display: flex;
  flex-direction: column;
}
.carousel-container {
  width: 95%;
}
.carousel__item {
  height: 60vh;
	color: rgb(165, 165, 165);
	font-size: 20px;
	border-radius: 8px;
	/* display: flex;
  flex-direction: row;
	justify-content: center;
	align-items: center; */
}
.carousel__prev,
.carousel__next {
  color: rgb(165, 165, 165);
}
.slideImg1 {
  margin-left: 20px;
}
.hi {
  margin-top: 40px;
}
</style>