<template>
  <Accordion>
    <AccordionPanel value="pk">
      <AccordionHeader>{{ header }}</AccordionHeader>
      <AccordionContent v-for="(item, item_id) in items" :key="item_id">
        <p class="m-0">
          {{ item }}
        </p>
      </AccordionContent>
    </AccordionPanel>
  </Accordion>
</template>

<script>
import Accordion from 'primevue/accordion';
import AccordionPanel from 'primevue/accordionpanel';
import AccordionHeader from 'primevue/accordionheader';
import AccordionContent from 'primevue/accordioncontent';

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
  },
  components: {
    Accordion, AccordionPanel, AccordionHeader, AccordionContent
  }
}
</script>