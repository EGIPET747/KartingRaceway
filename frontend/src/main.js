import { createApp } from 'vue'
import { createMemoryHistory, createRouter } from 'vue-router'
import axios from 'axios'

import './css/main.css'
import './css/bootstrap.min.css'

import App from './App.vue'
import AboutView from './components/about/AboutView.vue'
import MainView from './components/main/MainView.vue'


const routes = [
  { path: '/', name: "Main", component: MainView },
  { path: '/about', name: "About", component: AboutView },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

createApp(App)
  .use(router)
  .mount('#app')

axios.defaults.withCredentials = false;
axios.defaults.headers.post['Content-Type'] ='application/json;charset=utf-8';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
