<template>
  <div className="clubsPage">
    <div className="flex flex-row justify-content-between align-items-center">
      <h1 className="pageTitle">{{ pageName }}</h1>
      <Button label="Добавить клуб" @click="createClub" icon="pi pi-plus" iconPos="right" />
      <DynamicDialog />
    </div>
    <div className="wrapper">
      <div className="grid grid-nogutter surface-section">
        <ClubBlock v-for="(club, club_id) in clubs" :key="club_id" :club="club" :deleteClub="deleteClub" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Button from 'primevue/button'
import ClubBlock from "@/views/club/ClubBlock.vue"
import DynamicDialog from 'primevue/dynamicdialog';
import { inject } from 'vue'

export default {
  components: { Button, ClubBlock, DynamicDialog },
  props: {  },
  data() {
    return {
      name: "Клубы",
      clubs: [],
      API_URL: null,
    }
  },
  computed: {
    pageName() {
      return this.name;
    }
  },
  mounted() {
    this.API_URL = inject("API_URL");
    this.getClubs();
  },
  methods: {
    getClubs() {
      axios.get(this.API_URL + "api/club/list/").then(res => {
        this.clubs = res.data;
      })
    },
    deleteClub(pk) {
      axios.delete(this.API_URL + "api/club/", {data: pk});
      window.location.reload();
    }
  }
}
</script>

<script setup>
import { useDialog } from 'primevue/usedialog';
import CreateClubForm from '@/views/club/CreateClubForm.vue';

const dialog = useDialog();

const createClub = () => {
    dialog.open(CreateClubForm, {
        props: {
            header: "Добавление клуба",
            style: {
                width: '50vw',
            },
            breakpoints:{
                '960px': '75vw',
                '640px': '90vw'
            },
            modal: true
        }
    });
}
</script>
