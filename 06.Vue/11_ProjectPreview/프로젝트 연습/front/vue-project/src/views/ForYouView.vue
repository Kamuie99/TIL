<template>
	<main>
		<div class="main-container-big _2">
			<form @submit.prevent="submitForm" class="searchForm">
				<div class="form-inner">
					
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
	flex-direction: column;
	align-items: center;
	width: 100%;
	height: 100%;
}
.buttonSubmit {
	margin-top: 40px;
	font-size: 30px;
	cursor: pointer;
}
.form-inner {
	width: 100%;
	height: 85%;
	background-color: #1b1b1b;
	border-bottom-left-radius: 40px;
	border-bottom-right-radius: 40px;
}
</style>
