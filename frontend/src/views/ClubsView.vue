<template>
  <div className="clubsPage">
    <h1>{{ pageName }}</h1>
    <div className="wrapper">
        <div className="grid grid-nogutter surface-section">
          <ClubBlock v-for="(club, club_id) in clubs" :key="club_id" :club="club" :club_id="club_id" :deleteClub="deleteClub" />
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ClubBlock from "@/components/club/ClubBlock.vue"

export default {
  components: { ClubBlock },
  props: {
    API_URL: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      name: "Клубешники",
      clubs: []
    }
  },
  computed: {
    pageName() {
      return this.name;
    }
  },
  mounted() {
    this.getClubs();
  },
  methods: {
    getClubs() {
      axios.get(this.API_URL + "api/club/list/").then(res => {
        this.clubs = res.data;
      })
    },
    deleteClub() {
      alert("Никакого делита пока не реализуешь!")
    }
  }
}
</script>
