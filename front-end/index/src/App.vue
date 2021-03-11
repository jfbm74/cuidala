<template>
    <div id="app" class="wrapper">
      <Navegacion/>
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
