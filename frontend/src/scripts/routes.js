import AboutView from '@/views/AboutView.vue'
import UsersView from '@/views/UsersView.vue'
import MainView from '@/views/MainView.vue'


const routes = [{ 
    url: '/',
    path: '/', 
    label: "Main", 
    name: "Main",
    component: MainView,
    icon: "pi pi-home",
  },
  { 
    url: '/users',
    path: '/users', 
    label: "Users", 
    name: "Users",
    component: UsersView,
    icon: "pi pi-user",
  },
  { 
    url: '/about',
    path: '/about', 
    label: "About", 
    name: "About",
    component: AboutView,
    icon: "pi pi-question",
  }]

export default routes