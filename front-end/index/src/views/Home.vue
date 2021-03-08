<template>
    <div class="home">
        <SliderArea/>
        <NavService/>
        <Section/>
        <Contacto/>
        <Footer/>
    </div>
</template>

<script>
import Section from '@/components/Section.vue'
import NavService from '@/components/NavService.vue'
import SliderArea from '@/components/SliderArea.vue'
import Contacto from '@/components/Contacto.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'Home',
  components: {
    SliderArea,
    NavService,
    Section,
    Contacto,
    Footer
  }
}
</script>
