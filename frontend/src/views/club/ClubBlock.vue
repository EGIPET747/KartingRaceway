<template>
  <div className="col-12 p-2">
    <Card>
      <template #title>{{ club.name }}</template>
      <template #content>
        <Accordion :items="getAddressList(club.raceways)" :header="header" :pk="club.id" />
        <p><Button label="Удалить" @click="deleteClub(club.id)" icon="pi pi-trash" iconPos="right" /></p>
      </template>
    </Card>
  </div>
</template>

<script>
import Card from 'primevue/card';
import Button from 'primevue/button';
import Accordion from '@/components/Accordion.vue'

export default {
  name: "ClubBlock",
  data() {
    return {
      header: "Адреса клубешника",
    }
  },
  props: {
    club: {
      type: Object,
      required: true
    },
    deleteClub: {
      type: Function,
      required: true
    }
  },
  components: {
    Accordion, Button, Card
  },
  methods: {
    getAddressList(raceways) {
      let addressList = [];
      for(let rw in raceways){
        addressList.push(`${raceways[rw].city}, ${raceways[rw].address}`);
      }
      return addressList;
    }
  }
}
</script>