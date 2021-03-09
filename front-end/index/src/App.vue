<template>
    <div id="app">
      <div>
        <Navegacion/>
      </div>
      <router-view/>
    </div>
</template>

<script>
import Navegacion from '@/components/Navegacion.vue'

export default {
  name: 'App',
  components: {
    Navegacion,
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
