<template>
  <div id="wrapper">
    <MenuItems />
    <main>
      <div class="container">
        <RouterView :pageName="pageName" />
      </div>
    </main>
    <DynamicDialog />
    <ConfirmDialog></ConfirmDialog>
    <div id="footer" class="m-0 pb-2">
      <Footer />
    </div>
  </div>
</template>

<script>
import ConfirmDialog from 'primevue/confirmdialog';
import DynamicDialog from 'primevue/dynamicdialog';
import MenuItems from '@/components/MenuItems';
import Footer from '@/components/Footer.vue';

export default {
  name: 'App',
  data() {
    return {
      pageName: "Karting Raceway",
    }
  },
  components: {
    ConfirmDialog, DynamicDialog,
    Footer, MenuItems,
  },
  methods: {
    redirect(link){
      window.open(link, "_blank").focus();
    }
  }
}
</script>
<script setup>
  import { useToast } from 'primevue/usetoast';
  import { useConfirm } from 'primevue/useconfirm';
  import { useDialog } from 'primevue/usedialog';
  import { provide } from 'vue';

  const TOAST = useToast();
  const CONFIRM = useConfirm();
  const DIALOG = useDialog();

  // Мы можем навесить по одному шаблону диалогов и тостов на весь проект и дёргать их в любом месте!
  // Каеф :)
  provide("TOAST", TOAST);
  provide("CONFIRM", CONFIRM);
  provide("DIALOG", DIALOG);
</script>
<style>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

#wrapper {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 20px;
  margin-bottom: 20px;
}

.pageTitle {
  text-align: center;
}

#footer {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: fixed;
  bottom: 0;
  text-align: center;
  font-size: 19px;
  width: -webkit-fill-available;
}
</style>
