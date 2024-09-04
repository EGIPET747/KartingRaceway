<template>
  <div class="login">
    <input type="text" placeholder="Имя" v-model="userName">
    <br>
    <input type="email" placeholder="Email" v-model="userEmail">
    <br>
    <input type="password" placeholder="Пароль" v-model="userPass">
    <br>
    <button type="button" @click="sendUserData">Отправить данные</button>
    <div v-if="users.length == 0">Пользователей нет</div>
    <div v-else-if="users.length == 1">Единственный пользователь:</div>
    <div v-else>Список пользователей ({{ users.length }}):</div>
    <UserBlock v-for="(user, user_id) in users" :key="user_id" :user="user" :user_id="user_id" :deleteUser="deleteUser" />
  </div>
</template>

<script>
import UserBlock from "@/views/user/UserBlock.vue"

export default {
  name: 'AboutView',
  props: {  },
  components: { UserBlock },
  data() {
    return {
      users: [],
      userName: '',
      userPass: '',
      userEmail: '',
    }
  },
  methods: {
    sendUserData() {
      if(this.userName == ''){
        alert("Введите имя")
        return;
      }
      if(this.userEmail == ''){
        alert("Введите email")
        return;
      }
      if(this.userPass == ''){
        alert("Введите пароль")
        return;
      }
      this.users.push({
        name: this.userName,
        pass: this.userPass,
        email: this.userEmail,
      })
    },
    deleteUser(user_id){
      this.users.splice(user_id, 1);
    }
  }
}
</script>
