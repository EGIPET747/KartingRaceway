<template>
  <div id="wrapper">
    <MenuItems />
    <main>
      <div class="container">
        <RouterView :API_URL="API_URL" :pageName="pageName" />
      </div>
    </main>
    <div id="footer" class="m-0 pb-2">
      <Footer />
    </div>
  </div>
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

<style>
#wrapper {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 20px;
  margin-bottom: 20px;
}

.pageTitle {
  text-align: center;
}

#footer {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: fixed;
  bottom: 0;
  text-align: center;
  font-size: 19px;
  width: -webkit-fill-available;
}
</style>
