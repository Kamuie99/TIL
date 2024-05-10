import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ReviewSearchView from '@/views/ReviewSearchView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movies',
      name: 'movies',
      component: MovieListView
    },
    {
      path: '/:movieId',
      name: 'MovieDetail',
      component: MovieDetailView,
      props: true
    },
    {
      path: '/review-search',
      name: 'ReviewSearch',
      component: ReviewSearchView,
    }
  ]
})

export default router
