<template>
  <div>
    <label for="city" class="block text-900 font-medium mb-2">Город</label>
    <InputText id="city" v-model="racewayCity" type="text" class="w-full mb-3" />
    <label for="address" class="block text-900 font-medium mb-2">Адрес</label>
    <InputText id="address" v-model=racewayAddress type="text" class="w-full mb-3" />
  </div>
  <div className="flex flex-row justify-content-center">
    <Button label="Создать" @click="createRaceway()" iconPos="right" icon="pi pi-plus" class="w-full"></Button>
  </div>
</template>

<script>
import axios from 'axios';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { inject } from 'vue';

export default {
  name: "CreateRacewayForm",
  components: {
    Button, InputText
  },
  mounted() {
    const dialogRef = inject("dialogRef");
    this.club_id = dialogRef.value.data.club_id;
    this.API_URL = inject("API_URL");
  },
  data() {
    return {
        racewayCity: "",
        racewayAddress: "",
        club_id: 0,
        API_URL: null,
    }
  },
  methods: {
    createRaceway() {
      axios.post(this.API_URL + "api/raceway/", 
        {
          club_id: this.club_id,
          city: this.racewayCity,
          address: this.racewayAddress,
          description: {}
        }
      ).then(res => {
        console.log(res);
        if(res.status == 201){
          alert("Ну, крч, создали мы тебе трассу в городе: " + this.racewayCity);
          window.location.reload();
        }
      })
    }
  }
}
</script>
