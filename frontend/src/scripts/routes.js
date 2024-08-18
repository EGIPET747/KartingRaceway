import AboutView from '@/views/about/AboutView.vue'
import UsersView from '@/views/user/UsersView.vue'
import ClubsView from '@/views/club/ClubsView.vue'


const routes = [
  { 
    url: '/',
    path: '/', 
    label: "Clubs", 
    name: "Clubs",
    component: ClubsView,
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
  },
]

export default routes