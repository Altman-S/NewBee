import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MovieInfoPage from '../views/MovieInfoPage.vue'
import StartPage from '../views/StartPage.vue'
import NotFoundPage from '../views/NotFoundPage.vue'
import MovieListPage from '../views/MovieListPage.vue'
import MovieAllPage from "../views/MovieAllPage";


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
            {
                path: '/searchAll',
                name: 'MovieAllPage',
                component: MovieAllPage,
                props: true,
                meta: {
                    keepAlive: false
                }
            },
        ]
    },
     
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
