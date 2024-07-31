<template>
  <div id="app">.
    <div className="NavBar" style="display: block; position: absolute; top: 2px; left: 2px;">
      <div class="row">
        <div class="col">
          <h3>{{ projName }}</h3>
        </div>
        <nav>
          <RouterLink class="btn btn-light-info m-2" to="/">Go to Home</RouterLink>
          <RouterLink class="btn btn-light-info m-2" to="/about">Go to About</RouterLink>
        </nav>
      </div>
    </div>
    <main>
      <RouterView :API_URL="API_URL" />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    goToAbout() {
      this.$router.replace('/about')
    }
  },
  data() {
    return {
      projName: "Karting RaceWay",
      API_URL: process.env.VUE_APP_API_URL,
    }
  },
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h3 {
    font-weight: lighter;
}
</style>
