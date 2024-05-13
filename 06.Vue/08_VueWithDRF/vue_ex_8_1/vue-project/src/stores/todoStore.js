import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useTodoStore = defineStore('todo', () => {
  const todos = ref([])
  const BASE_URL = 'http://127.0.0.1:8000'

  const getTodos = () => {
    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/todos/`
    })
      .then(response => {
        console.log(response)
        todos.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
  return { todos, BASE_URL, getTodos }
}, { persist: true })
