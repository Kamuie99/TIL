<template>
    <div>
        <p>이름: {{ balance.name }}</p>
        <p>잔고: {{ balance.balance }}</p>
        <button @click="goToUpdateView(balance)">updateBalance</button>
        <hr>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

defineProps({
    balance: Object
})

const router = useRouter()

const goToUpdateView = (balance) => {
    router.push({ name: 'update', params: {name : balance.name }})
}
</script>

<style scoped>

</style>