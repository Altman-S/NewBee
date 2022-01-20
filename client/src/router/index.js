import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MovieInfoPage from '../views/MovieInfoPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/movie/:id',
    name: 'Movie',
    component: MovieInfoPage,
    props:true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
