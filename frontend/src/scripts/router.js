import { createWebHistory, createRouter } from 'vue-router'

import AboutView from '@/views/AboutView.vue'
import UsersView from '@/views/UsersView.vue'
import MainView from '@/views/MainView.vue'


const routes = [
  { path: '/', name: "Main", component: MainView },
  { path: '/users', name: "Users", component: UsersView },
  { path: '/about', name: "About", component: AboutView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router