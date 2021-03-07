<template>
    <div class="contacto">
        <img src="../assets/banner2.jpg" alt="banner2">
        <div id="cuadrado-contacto"> </div>
        <h4>Solicita Información</h4>
        <p>Déjanos tus datos y nos pondremos en contacto contigo</p>
        <div class="formulario">
            <input type="text" id="Nombre" name="Nombre" placeholder="Nombre">
            <input type="text" id="apellido" name="apellido" placeholder="Apellido">
            <input type="number" id="telefono" name="telefono" placeholder="Telefono">
            <input type="email" id="email" name="email" placeholder="Email">
            <input type="text" id="cuentanos" name="cuentanos" placeholder="Cuentanos algo sobre lo que necesitas">
            <input type="submit" id="submit" value="Solicita información">
        </div>
    </div>
</template>

<script>
export default {
  name: 'Contacto'
}
</script>

<style scoped>
.contacto {
  width: 100%;
  height: 603px;
}
.contacto img {
  width: 100%;
  height: 603px;
}
.contacto #cuadrado-contacto {
  width: 100%;
  height: 603px;
  background: #598f8f;
  opacity: 0.9;
  position: relative;
  bottom: 607px;
}

.contacto h4 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 29px;
  color: #fff;
  margin: 0px;  
  bottom: 500px;position: relative;
  margin-left: 50px;
  position: relative;
  bottom: 1100px;
  text-align: left;
}
.contacto p {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 17px;
  bottom: 530px;
  color: #ffffff;
  position: relative;
  bottom: 1100px;
  text-align: left;
  margin-left: 50px;
  margin-top: 20px;

}
.formulario {
    width: 500px;
    height: 400px;
    position: relative;
    bottom: 1080px;
}
input {
  border: 0px;
  border-radius: 5px;
  background: #e5f5f7;
  outline: none;
  margin: 10px;
  height: 40px;
}
input#cuentanos {
    width: 300px;
    height: 200px;
    margin-right: 65px;
    
}
input#submit {
    background: #efd240;
    height: 40px;
    margin-left: 60px;
    margin-right: 130px;
    
}
</style>