import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import QuizView from '@/views/QuizView.vue';
import AnswerView from '@/views/AnswerView.vue';



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/quiz',
      name: 'Quiz',
      component: QuizView,
    },
    {
      path: '/answer/:pk/:answer',
      name: 'AnswerView',
      component: AnswerView
    },
  ]
})

export default router
