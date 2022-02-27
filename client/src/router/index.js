import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MovieInfoPage from '../views/MovieInfoPage.vue'
import StartPage from '../views/StartPage.vue'
import ErrorPage from '../views/ErrorPage.vue'


const routes = [
  {
    path: '/',
    name: 'StartPage',
    component: StartPage,
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: {
      keepAlive: true,
    }
  },
  {
    path: '/movie/:id',
    name: 'MovieInfoPage',
    component: MovieInfoPage,
    props: true,
    meta: {
      keepAlive: false
    }
  },
  {
    path: '/errorpage',
    name: 'ErrorPage',
    component: ErrorPage,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
