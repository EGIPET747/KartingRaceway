<template>
  <div className="clubsPage">
    <div className="flex flex-row justify-content-between align-items-center">
      <h1 className="pageTitle">{{ pageName }}</h1>
      <Button label="Добавить клуб" @click="createClub" icon="pi pi-plus" iconPos="right" />
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
import Button from 'primevue/button';
import ClubBlock from "@/views/club/ClubBlock.vue";
import { inject } from 'vue';

export default {
  components: { Button, ClubBlock },
  props: {  },
  data() {
    return {
      name: "Клубы",
      clubs: [],
      API_URL: null,
      toast: null,
      confirm: null,
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
    this.toast = inject("TOAST");
    this.confirm = inject("CONFIRM");
  },
  methods: {
    getClubs() {
      axios.get(this.API_URL + "api/club/list/").then(res => {
        this.clubs = res.data;
      })
    },
    deleteClub(pk) {
      this.confirm.require({
        header: ":(",
        message: 'Уверен, что хочешь удалить клуб?',
        icon: 'pi pi-info-circle',
        rejectLabel: 'Нет, отмена!',
        rejectProps: {
            label: 'Cancel',
            severity: 'secondary',
            outlined: true
        },
        acceptProps: {
            label: 'Да, удоли!',
            severity: 'danger'
        },
        accept: () => {
          axios.delete(this.API_URL + "api/club/", {data: pk});
          window.location.reload();
        },
        reject: () => {
          this.toast.add({ severity: 'error', summary: 'Rejected', detail: 'Фух, не удалили', life: 3000 });
        }
      });
    }
  }
}
</script>

<script setup>
import CreateClubForm from '@/views/club/CreateClubForm.vue';

const dialog = inject("DIALOG");

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
