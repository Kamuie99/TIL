<template>
  <div class="boxoffice-container _cont2">
		<div class="carousel-container2">
			<p class="boxoffice-title">Box Office</p>
			<Carousel :autoplay="1000" :itemsToShow="5" :wrapAround="true" :transition="500">
				<Slide v-for="slide in slides" :key="slide">
					<div class="carousel__item2">
						<img :src="slide" class="slideImg">	
					</div>
				</Slide>
				<template #addons>
					<navigation />
				</template>
			</Carousel>
		</div>
  </div>
</template>

<script setup>
import { defineComponent, ref } from 'vue'
import { Carousel, Pagination, Slide, Navigation } from 'vue3-carousel'
import "vue3-carousel/dist/carousel.css";
import img_1 from '@/assets/movie1.jpg'
import img_2 from '@/assets/movie2.jpg'
import img_3 from '@/assets/movie3.jpg'
import img_4 from '@/assets/movie4.jpg'
import img_5 from '@/assets/movie1.jpg'
import img_6 from '@/assets/movie2.jpg'
import img_7 from '@/assets/movie3.jpg'
import img_8 from '@/assets/movie4.jpg'

const slides = ref([img_1, img_2, img_3, img_4, img_5, img_6, img_7, img_8])

defineComponent({
  name: 'BoxOffice',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
});

</script>

<style scoped>
.boxoffice-container {
	height: 45vh;
}
.carousel-container2 {
	width: 100%;
}
.boxoffice-title {
	margin-bottom: 40px;
	margin-left: 40px;
	font-size: 17px;
	color: rgb(165, 165, 165);
}
._cont2 {
	display: flex;
	justify-content: center;
	align-items: center;
}
.slideImg {
  width: 200px;
}
.carousel__item2 {
	width: 300px;
	height: 300px;
	display: flex;
	justify-content: center;
	align-items: center;
}
</style>