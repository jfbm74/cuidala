<template>
    <div class="app">
        <Navegacion/>
        <SliderArea/>
        <NavService/>
        <Section/>
        <Contacto/>
        <Footer/>
    </div>
</template>

<script>
import Navegacion from '@/components/Navegacion.vue'
import Section from '@/components/Section.vue'
import NavService from '@/components/NavService.vue'
import SliderArea from '@/components/SliderArea.vue'
import Contacto from '@/components/Contacto.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'App',
  components: {
    Navegacion,
    SliderArea,
    NavService,
    Section,
    Contacto,
    Footer
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
