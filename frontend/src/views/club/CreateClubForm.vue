<template>
  <div>
    <label for="name" class="block text-900 font-medium mb-2">Название</label>
    <InputText id="name" v-model="clubName" type="text" class="w-full mb-3" />
  </div>
  <div className="flex flex-row justify-content-center">
    <Button label="Создать" @click="createClub" iconPos="right" icon="pi pi-plus" class="w-full"></Button>
  </div>
</template>

<script>
import axios from 'axios';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { inject } from 'vue'

export default {
  name: "CreateClubForm",
  components: {
    Button, InputText
  },
  data() {
    return {
      clubName: null,
      API_URL: null,
    }
  },
  props: {  },
  methods: {
    createClub() {
      if(! this.clubName){
        alert("Город название, для начала");
        return;
      }
      axios.post(this.API_URL + "api/club/", {name: this.clubName, description: {}}).then(res => {
        console.log(res);
        if(res.status == 201){
          alert("Ну, крч, создали мы тебе клуб: " + this.clubName);
          window.location.reload();
        }
      });
    }
  },
  mounted() {
    this.API_URL = inject("API_URL");
  }
}
</script>