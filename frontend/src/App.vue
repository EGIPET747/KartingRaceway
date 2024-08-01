<template>
  <div id="wrapper">
    <MenuItems />
    <main>
      <div class="container">
        <RouterView :API_URL="API_URL" />
      </div>
    </main>
  </div>
  <Footer id="footer" />
</template>

<script>
import MenuItems from '@/components/MenuItems';
import Footer from '@/components/Footer.vue';

export default {
  name: 'App',
  data() {
    return {
      projName: "Karting RaceWay",
      API_URL: process.env.VUE_APP_API_URL,
    }
  },
  components: {
    Footer, MenuItems,
  },
  methods: {
    redirect(link){
      window.open(link, "_blank").focus();
    }
  }
}
</script>

<style scoped>
#wrapper {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 20px;
}

#footer {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  position: fixed;
  right: 0;
  bottom: 0;
  text-align: center; 
  width: 99%;   
  font-size: 19px;
}
</style>
