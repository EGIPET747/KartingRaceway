<template>
  <div className="mainPage">
    <h3>Заголовок страницы через свойство:</h3>
    <h1>{{ pageName }}</h1>
    <div className="wrapper">
      <h1>Обращение по АПИ</h1>
      <p>Тестим апишные запросы</p>
      <p>{{ currentDatetime }}</p>
      <input type="text" placeholder="Введи чё хош" v-model="name">
      <button type="button" @click="getDatetime()">Кликни меня</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { inject } from 'vue'

export default {
  props: {  },
  data() {
    return {
      name: "Проверка АПИ",
      currentDatetime: null,
      API_URL: null,
    }
  },
  computed: {
    pageName() {
      return `"${this.name}"`;
    }
  },
  mounted() {
    this.API_URL = inject("API_URL");
  },
  methods: {
    getDatetime() {
      axios.get(this.API_URL + "api/base/current_datetime/").then(res => {
        this.currentDatetime = res.data;
      })
    },
  }
}
</script>
