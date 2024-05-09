import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  // const products = ref([
  //   { id: 1, title: 'Product 1', body: 'quia et suscipit suscipit recusandae' },
  //   { id: 2, title: 'Product 2', body: 'quo iure voluptatem occaecati omnis' },
  //   { id: 3, title: 'Product 3', body: 'repudiandae veniam quaerat sunt' }
  // ])
  const products = ref([])

  const fetchProducts = async () => {
    try {
      // APi 요청을 보내는 부분
      const response = await axios.get('https://jsonplaceholder.typicode.com/posts')
      // 응답 데이터를 'products' 상태로 업데이트
      products.value = response.data
    } catch (error) {
      console.error('error: ', error)
    }
  }

  // 초기에 제품 가져오기
  fetchProducts()

  const productCount = computed(() => products.value.length)

  const deleteProduct = function (productId) {
    // 요소를 직접 수정하는 대신에 splice 메서드를 사용하여 새로운 배열을 생성하여 상태를 업데이트
    const index = products.value.findIndex(product => product.id === productId)
    if (index !== -1) {
      products.value.splice(index, 1)
    }
  }

  return { products, productCount, deleteProduct }
})
