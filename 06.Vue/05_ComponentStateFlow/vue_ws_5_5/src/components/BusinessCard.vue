<template>
  <businessCardDetail class="card_detail" :people="businessCards" @delete-card="deletePerson" v-if="businessCards.length > 0"/>
  <p v-else>명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
</template>

<script setup>
import businessCardDetail from '@/components/businessCardDetail.vue'
import { ref, watch } from 'vue'

const props = defineProps({
  people: Array
})

const emit = defineEmits(['delete-card'])
const businessCards = ref(props.people)

watch(
  () => props.people,
  (newVal) => {
    businessCards.value = newVal
  },
  { immediate: true }
)

const deletePerson = (person) => {
  emit('delete-card', person)
}
</script>
