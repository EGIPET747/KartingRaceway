import { createWebHistory, createRouter } from 'vue-router'
import routes from '@/scripts/routes'

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router