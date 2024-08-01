import { createApp } from 'vue'
import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';
import axios from 'axios'

import 'primeicons/primeicons.css'
import '@/css/main.css'

import router from '@/scripts/router';

import App from '@/App.vue'

const app = createApp(App)

app.use(router)
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
  })

app.mount('#app')

axios.defaults.withCredentials = false;
axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
