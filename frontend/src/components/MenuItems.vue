<template>
    <div className="NavBar" style="display: block; position: absolute; top: 2px; left: 2px;">
      <div class="row">
        <div class="col">
          <h3>{{ projName }}</h3>
        </div>
        <div id="nav">
          <router-link to="/">Home</router-link> |
          <router-link to="/users">Users</router-link> |
          <router-link to="/about">About</router-link>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "MenuItems",
  methods: {

  },
  props: {
    projName: {
        type: String,
        required: true,
    }
  },
  data() {
    return {
    }
  }
}
</script>