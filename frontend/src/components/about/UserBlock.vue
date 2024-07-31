<template>
    <div className="">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
      <p><button type="button" @click="deleteUser(user_id)">Удалить</button></p>
    </div>
</template>

<script>
export default {
  name: "UserBlock",
  props: {
    user: {
      type: Object,
      required: true
    },
    user_id: {
      type: Number,
      required: true
    },
    deleteUser: {
      type: Function,
      required: true
    }
  },
}
</script>

<style scoped>

</style>