<template>
  <!-- banner -->
  <div class="banner">
    <h3>
    Cuidado de <br> personas <br> a domicilio
    </h3>
    <p>Eres más que <br> importante</p>
    <div class="style">
      <span class="icon"><i class="fa fa-search"></i></span>
      <input id="search" class="centrado" type="search" name="Busqueda" placeholder="Busqueda">
    </div>
  </div>
  <!-- end banner -->
</template>

<script>
export default {
  name: 'SliderArea'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    color: #28808a;
    font-size: 70px;
    margin: 0px 50px 0px 50px;
    padding-top: 80px;
    text-align: left;
}
p {
    font-size: 40px;
    margin: 0 50px 0 50px;
    padding-top: 50px;
    text-align: left;
}
.banner {
  background-image: url('../assets/banner.jpg');
  margin: 0 auto;
  width: 100%;
  height: 750px;
}
.style {
    width: 300px;
    vertical-align: center;
    white-space: nowrap;
    position: relative;
}
.style input {
    width: 400px;
    height: 50px;
    background: #28808a;
    border: none;
    font-size: 10pt;
    float: left;
    color: #63717f;
    padding-left: 45px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 15px;
    margin-left: 150%;
}

.centrado {
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.style .icon{
    position: absolute;
    top: 50%;
    margin-left: 17px;
    margin-top: 17px;
    z-index: 1;
    color: #000;
    margin-left: 155%;
}
.style input#search:hover, .style input#search:focus, .style input#search:active {
    outline: none;
    background: #ffffff;
}
.style input#search::-webkit-input-placeholder {
    color: #ffffff;
}
</style>