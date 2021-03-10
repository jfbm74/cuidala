<template>
  <div id="app">
    <header>
      <ul>
        <li><a href="#"> <router-link to="/">Inicio </router-link></a></li>
        <li><a href="#">Sobre Nosotros</a></li>
        <li><a href="#">Cuidadores</a></li>
        <li><a href="#">Contacto</a></li>
        <li><a > <router-link to="/registro">Reg&iacute;strate </router-link></a></li>
        <li><a><router-link to="/login">Login</router-link></a></li>
        
      </ul>
    </header>
  </div>
</template>

<script>
export default {
  name: 'Navegacion',
}
</script>


<style scoped>
ul {
  margin: 10px 20px 10px 20px;
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