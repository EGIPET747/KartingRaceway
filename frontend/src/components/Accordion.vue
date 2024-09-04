<template>
  <Accordion>
    <AccordionPanel value="pk">
      <AccordionHeader>{{ header }}</AccordionHeader>
      <AccordionContent>
        <div class="mb-3" v-for="(item, item_id) in items" :key="item_id">
          {{ item }}
          <hr />
        </div>
        <Button :label="aBText" @click="aBMethod(aBArgs)" icon="pi pi-plus" iconPos="right" />
      </AccordionContent>
    </AccordionPanel>
  </Accordion>
</template>

<script>
import Accordion from 'primevue/accordion';
import AccordionPanel from 'primevue/accordionpanel';
import AccordionHeader from 'primevue/accordionheader';
import AccordionContent from 'primevue/accordioncontent';
import Button from 'primevue/button';

export default {
  name: "AAccordion",
  props: {
    items: {
      type: Object,
      required: true
    },
    pk: {
      type: Number,
      required: true
    },
    header: {
      type: String,
      required: true
    },
    aBText: {
      type: String,
      required: true
    },
    aBMethod: {
      type: Function,
      required: true
    },
    aBArgs: {
      type: Object,
      required: true
    },
  },
  components: {
    Accordion, AccordionPanel, AccordionHeader, AccordionContent, Button
  }
}
</script>