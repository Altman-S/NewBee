import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MovieInfoPage from '../views/MovieInfoPage.vue'
import StartPage from '../views/StartPage.vue'
<<<<<<< HEAD
import NotFoundPage from '../views/NotFoundPage.vue'
import MovieListPage from '../views/MovieListPage.vue'


const routes = [
    {
        path: '/',
        name: 'StartPage',
        component: StartPage,
        meta: {
            keepAlive: false,
        }
    },
    {
        path: '/home',
        name: 'Home',
        component: Home,
        meta: {
            keepAlive: true,
        },
        children:[
            {
                path:'search',
                name: 'MovieListPage',
                component:MovieListPage,
                meta: {
                    keepAlive: true
                },
            },
            {
                path: '/notfound/:searchtxt',
                name: 'NotFoundPage',
                component: NotFoundPage,
                props: true,
                meta: {
                    keepAlive: false
                },
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
        ]
    },
     
=======
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
>>>>>>> 7ac582f659507b6eb019d470416b2f99c25484f1
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
