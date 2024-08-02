<template>
  <footer class="mr-2">
    <Fieldset legend="Karting RaceWay" :toggleable="false">
        <div id="links">
            <Button icon="pi pi-telegram" aria-label="Filter" @click="redirect('https://t.me/kazakov_id')" />
            <Button icon="pi pi-github" aria-label="Filter" @click="redirect('https://github.com/EGIPET747')" />
        </div>
    </Fieldset>
  </footer>
</template>

<script>
import Button from 'primevue/button';
import Fieldset from 'primevue/fieldset';

export default {
    name: 'AboutView',
    components: { 
        Button,
        Fieldset,
    },
    methods: {
        redirect(link){
        window.open(link, "_blank").focus();
        }
    }
}
</script>

<style scoped>
#links button {
  margin: 0px 5px 0px 5px;
}
</style>