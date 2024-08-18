<template>
    <div className="">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
      <p><Button label="Удалить" @click="deleteUser(user_id)" icon="pi pi-trash" iconPos="right" /></p>
    </div>
</template>

<script>
import Button from 'primevue/button';

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
  components: {
    Button,
  }
}
</script>