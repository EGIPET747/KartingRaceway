import { createApp } from 'vue'
import PrimeVue from 'primevue/config';
import Ripple from 'primevue/ripple';
import Aura from '@primevue/themes/aura';
import axios from 'axios'

import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css';
import '@/css/main.css'

import router from '@/scripts/router';

import App from '@/App.vue'

const app = createApp(App)

app.use(router)
app.use(PrimeVue, {
    ripple: true,
    theme: {
        preset: Aura,
        options: {
            prefix: 'p',
            darkModeSelector: 'system',
            cssLayer: false
        }
    }
  })
app.directive('ripple', Ripple)

app.mount('#app')

axios.defaults.withCredentials = false;
axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
