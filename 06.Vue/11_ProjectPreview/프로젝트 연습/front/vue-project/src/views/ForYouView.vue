<template>
	<main>
		<div class="main-container-big _1">
			<form @submit.prevent="submitForm" class="searchForm">
				<div>
					<!-- 추후 작성 예정-->
				</div>
				<input type="submit" value="제출" class="buttonSubmit">
			</form>
		</div>
		<div class="main-container-big _2" ref="bottomDiv">
			<RecommendMovie/>
		</div>
	</main>
</template>

<script setup>
import { ref } from 'vue';
import RecommendMovie from '@/components/RecommendMovie.vue'

const bottomDiv = ref(null);

const submitForm = () => {
// 아래쪽 div로 스크롤 이동
	bottomDiv.value.scrollIntoView({ behavior: 'smooth' });
};
</script>

<style scoped>
.main-container {
	height: 46vh;
}
.main-container-big {
	height: 92vh;
}
._1 {
	background-color: #1b1b1b;	
}
._2 {
	background-color: #E5DFCC;
}
.searchForm {
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100%;
	height: 100%;
}
.buttonSubmit {
	font-size: 50px;
}
</style>
