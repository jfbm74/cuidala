<template>
  <div id="app">
    <header>
      <ul>
        <li><a href="#">Inicio</a></li>
        <li><a href="#">Sobre Nosotros</a></li>
        <li><a href="#">Cuidadores</a></li>
        <li><a href="#">Contacto</a></li>
        <li><a href="registro.html">Reg&iacute;strate</a></li>
        <li><a href="#">Login</a></li>
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