<template>
  <div className="col-6 p-2">
    <Card>
      <template #title>{{ club.name }}</template>
      <template #content>
          <p><Button label="Удалить" @click="deleteClub(club_id)" icon="pi pi-trash" iconPos="right" /></p>
      </template>
    </Card>
  </div>
</template>

<script>
import Card from 'primevue/card';
import Button from 'primevue/button';

export default {
  name: "ClubBlock",
  props: {
    club: {
      type: Object,
      required: true
    },
    club_id: {
      type: Number,
      required: true
    },
    deleteClub: {
      type: Function,
      required: true
    }
  },
  components: {
    Button, Card
  }
}
</script>