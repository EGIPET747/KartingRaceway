<template>
  <div className="col-12 py-2">
    <Card>
      <template #title>{{ club.name }}</template>
      <template #content>
        <Accordion
         :items="getAddressList(club.raceways)"
         :header="header"
         :pk="club.id"
         :aBText="addRacewayText"
         :aBMethod="createRacewayDialog"
         :aBArgs="{club_id: club.id}" />
        <div className="flex py-2 flex-row justify-content-between">
          <Button label="Удалить" @click="deleteClub(club.id)" severity="danger" icon="pi pi-trash" iconPos="right" />
        </div>
      </template>
    </Card>
  </div>
</template>

<script>
import Accordion from '@/components/Accordion.vue';
import Button from 'primevue/button';
import Card from 'primevue/card';
// import DynamicDialog from 'primevue/dynamicdialog';


export default {
  name: "ClubBlock",
  data() {
    return {
      header: "Трассы клуба",
      addRacewayText: "Добавить трассу",
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
    Accordion, Button, Card, 
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

<script setup>
import { useDialog } from 'primevue/usedialog';
import CreateRacewayForm from '@/views/club/CreateRacewayForm.vue';

const dialog = useDialog();

const createRacewayDialog = (data) => {
    dialog.open(CreateRacewayForm, {
        props: {
            header: "Добавление трассы",
            style: {
                width: '50vw',
            },
            breakpoints:{
                '960px': '75vw',
                '640px': '90vw'
            },
            modal: true
        },
        data: data,
    });
}
</script>
