import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MovieInfoPage from '../views/MovieInfoPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta:{
      keepAlive:true,
    }
  },
  {
    path: '/movie/:id',
    name: 'MovieInfoPage',
    component: MovieInfoPage,
    props:true,
    meta:{
      keepAlive:false
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router