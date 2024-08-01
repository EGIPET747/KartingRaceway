<template>
  <div id="wrapper">
    <MenuItems :projName="projName" />
    <main>
      <div class="container">
        <RouterView :API_URL="API_URL" />
      </div>
    </main>
  </div>
</template>

<script>
import MenuItems from '@/components/MenuItems';

export default {
  name: 'App',
  data() {
    return {
      projName: "Karting RaceWay",
      API_URL: process.env.VUE_APP_API_URL,
    }
  },
  components: {
    MenuItems,
  }
}
</script>

<style scoped>
#wrapper {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
</style>
