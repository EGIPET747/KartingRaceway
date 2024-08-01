<template>
  <Menubar :model="items" />
</template>

<script>
import Menubar from 'primevue/menubar';
import routes from "@/scripts/routes.js";

export default {
  name: "MenuItems",
  components: {
    Menubar
  },
  data() {
    return {
      items: routes,
    }
  }
}
</script>