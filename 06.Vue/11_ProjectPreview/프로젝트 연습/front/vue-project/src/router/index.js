import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ForYouView from '@/views/ForYouView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/foryou',
      name: 'foryou',
      component: ForYouView
    }
  ]
})

router.afterEach(() => {
  window.scrollTo(0, 0); // 페이지 최상단으로 스크롤
});

export default router
