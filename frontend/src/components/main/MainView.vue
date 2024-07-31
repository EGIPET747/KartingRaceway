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

export default {
  props: {
    API_URL: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      name: "Проверка АПИ",
      currentDatetime: ""
    }
  },
  computed: {
    pageName() {
      return `"${this.name}"`;
    }
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

<style scoped>
.wrapper {
  width: 900px;
  height: 500px;
  border-radius: 50px;
  border: 1px solid black;
  padding: 20px;
  background-color: azure;
}

.wrapper h1 {
  margin-top: 50px;
}

.wrapper p {
  margin-top: 20px;
}

.wrapper input {
  margin-top: 20px;
  background: transparent;
  border: 0;
  border-bottom: 2px solid black;
  font-size: 14px;
  padding: 5px 14px;
  outline: none;
}

.wrapper input:focus {
  border-bottom: 2px solid grey;
}

.wrapper button {
  background: lightgreen;
  border-radius: 15px;
  border: 1px solid black;
  font-size: 14px;
  padding: 5px 14px;
  outline: none;
  cursor: pointer;

  transition: transform 150ms ease;
}

.wrapper button:hover {
  border-bottom: 2px solid grey;
  transform: scale(1.05);
}
</style>
