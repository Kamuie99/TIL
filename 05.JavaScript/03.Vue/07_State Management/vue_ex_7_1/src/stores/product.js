import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  let id = 1;
  const products = ref([
    {
      id,
      title: `Product ${id++}`,
      body: 'quia et suscipit suscipit recusandae'
    },
    {
      id,
      title: `Product ${id++}`,
      body: 'quo iure voluptatem occaecati omnis'
    },
    {
      id,
      title: `Product ${id++}`,
      body: 'repudiandae veniam quaerat sunt'
    },
  ])
  return { products }
})
