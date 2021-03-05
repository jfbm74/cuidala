<template>
   <nav>
		<ul>
			<li><a href="#">CUIDADO DE ANCIANOS</a></li>
			<li><a href="#">SERVICIOS ESPECIALES</a></li>
			<li><a href="#">ACOMPAÑAMIENTO</a></li>
		</ul>
		</nav> 
</template>

<script>

export default {
  name: 'NavService'
}

</script>

<style scoped>
  nav {
      text-align: center;
      background-color: #28808a;
  }
  ul {
    margin: 100px 20px 100px 20px;
    list-style: none;
    display: inline-block; 
  }
  ul li {
  list-style: none;
  font-family: Arial;
  float: left;
}
ul li a {
  color: white;
  text-decoration: none;
  padding: 10px 180px 10px 20px;
}
</style>