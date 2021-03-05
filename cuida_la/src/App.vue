<template>
  <div id="app">
    <header>
      <ul>
        <li><a href="#">Inicio</a></li>
        <li><a href="#">Sobre Nosotros</a></li>
        <li><a href="#">Cuidadores</a></li>
        <li><a href="#">Contacto</a></li>
        <li><a href="#">Reg&iacute;strate</a></li>
        <li><a href="#">Login</a></li>
      </ul>
    </header>
    <slider-area/>
    <nav-service/>
    <contact-form/>
    <router-view/>
  </div>
</template>

<script>
import SliderArea from '@/components/SliderArea'
import NavService from './components/NavService.vue'
import ContactForm from './components/ContactForm.vue'

export default {
  components: {
    SliderArea,
    NavService,
    ContactForm
  },
  name: 'App'
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
#app .banner {
  background-image: url('../src/assets/banner.jpg');
  margin: 0 auto;
  width: 100%;
  height: 850px;
}

ul {
  margin: 20px 20px 20px 20px;
  float: right;
}

ul li {
  list-style: none;
  font-family: Arial;
  float: left;
}

ul li a {
  color: grey;
  text-decoration: none;
  padding: 10px;
}

ul li a:hover {
  background-color: #AAAAAA;
  border-radius: 10px;
}
</style>
