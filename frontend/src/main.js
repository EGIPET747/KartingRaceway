import { createApp } from 'vue'
import App from './App.vue'
import { createMemoryHistory, createRouter } from 'vue-router'

import AboutView from './components/about/AboutView.vue'
import MainView from './components/main/MainView.vue'

const routes = [
  { path: '/', component: MainView },
  { path: '/about', component: AboutView },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

createApp(App)
  .use(router)
  .mount('#app')