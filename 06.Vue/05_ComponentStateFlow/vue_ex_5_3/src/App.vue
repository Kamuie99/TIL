<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList 
      :products="products"
      @addToCart = "addToCart"
    />
  </div>
  <div>
    <p>총 가격 : {{ totalPrice }}원</p>
    <h1>장바구니</h1>
    <Cart 
      :products="carts"
      @delete-item = "deleteItem"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from './components/Cart.vue';

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const carts = ref([]);

const totalPrice = ref(0);

const addToCart = (product) => {
  carts.value.push(product)
  totalPrice.value += product.price
}

const deleteItem = (product) => {
  const index = carts.value.indexOf(product)
  if (index !== -1) {
    const deleteProduct = carts.value.splice(index, 1)[0]
    totalPrice.value -= deleteProduct.price
  }
}


</script>
