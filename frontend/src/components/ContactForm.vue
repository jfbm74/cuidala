<template>
<!-- section -->
  <div>
    <div class="section1">
      <h3 clas="section-title">
        Tenemos el cuidador ideal para <br> cada personas
      </h3>
      <div class="cuadrado"></div>
      <p>
        Cuida.la quiere haceros facil lo que parecía dificil. Desde Cuida.la<br>
        los ayudaremos a encontrar el cuidador de personas ideal para<br>
        vuestra familia. Queremos daros la tranquilidad de tus seres<br>
        queridos los caules estarán en las mejores manos.
      </p>
      <img class="size-img" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNTEyIDUxMjsiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPHBhdGggc3R5bGU9ImZpbGw6I0ZGREIwQzsiIGQ9Ik0yNTYsNTEyTDI1Niw1MTJjMTM5LjY5NS01Mi4yNTgsMjMyLjI3Ni0xODUuNzM5LDIzMi4yNzYtMzM0Ljg4N1Y4Ni43MTYNCgljLTQ3Ljg5MiwwLTg2LjcxNi0zOC44MjQtODYuNzE2LTg2LjcxNkgyNTZIMTEwLjQ0YzAsNDcuODkyLTM4LjgyNCw4Ni43MTYtODYuNzE2LDg2LjcxNnY5MC4zOTYNCglDMjMuNzI0LDMyNi4yNjEsMTE2LjMwNSw0NTkuNzQyLDI1Niw1MTJMMjU2LDUxMnoiLz4NCjxwYXRoIHN0eWxlPSJmaWxsOiNGQkJGMDA7IiBkPSJNMjU2LDUxMkwyNTYsNTEyYzEzOS42OTUtNTIuMjU4LDIzMi4yNzYtMTg1LjczOSwyMzIuMjc2LTMzNC44ODdWODYuNzE2DQoJYy00Ny44OTIsMC04Ni43MTYtMzguODI0LTg2LjcxNi04Ni43MTZIMjU2QzI1NiwwLDI1NiwzOTgsMjU2LDUxMkwyNTYsNTEyeiIvPg0KPHBvbHlnb24gc3R5bGU9ImZpbGw6I0YxRjFGMjsiIHBvaW50cz0iMjIzLjY0MiwzNDYuMjgxIDE0Ni42NCwyNjkuMjggMTg5LjA2NiwyMjYuODUzIDIyMy42NDIsMjYxLjQyOSAzMjIuOTM0LDE2Mi4xMzcgDQoJMzY1LjM2LDIwNC41NjMgIi8+DQo8cG9seWdvbiBzdHlsZT0iZmlsbDojRTZFNkU2OyIgcG9pbnRzPSIyNTYsMzEzLjkyMyAyNTYsMjI5LjA3MSAzMjIuOTM0LDE2Mi4xMzcgMzY1LjM2LDIwNC41NjMgIi8+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8L3N2Zz4NCg==" />
      <p class="img-parrafo">
        Un servicio de asistencia a domicilio de calidad para<br>
        cuidar a las personas como se merecen
      </p>
    <div class="section-img">
      <img src="../assets/banner1.jpg" alt="banner1">
    </div>
    </div>
  </div>
  <!-- end section -->
  <!-- Contacto -->
  <div class="contacto">
    <img src="../assets/banner2.jpg" alt="banner2">
    <div id="cuadrado-contacto"> </div>
    <h4>Solicita Información</h4>
    <p>Déjanos tus datos y nos pondremos en contacto contigo</p>
    <input type="text" id="Nombre" name="Nombre" placeholder="Nombre">
    <input type="text" id="apellido" name="apellido" placeholder="Apellido">
    <input type="number" id="telefono" name="telefono" placeholder="Telefono">
    <input type="email" id="email" name="email" placeholder="Email">
    <input type="text" id="cuentanos" name="cuentanos" placeholder="Cuentanos algo sobre lo que necesitas">
    <input type="submit" id="submit" value="Solicita información">
    
  </div>
  <!-- end contacto -->

</template>

<script>
export default {
  name: 'ContactForm',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    color: #28808a;
    font-size: 70px;
    margin: 0px 50px 0px 50px;
    padding-top: 80px;
}
p {
    font-size: 40px;
    margin: 0 50px 0 50px;
    padding-top: 50px;
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
.section1 {
  width: 680px;
  height: 468px;
}
.section1 h3 {
  font-size: 28px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
.section1 p {
  font-size: 15px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  padding-top: 20px;
}
.size-img{
  margin-left: 70px;
  margin-top: 15px;
  height: 20px;
}
.section1 .img-parrafo {
  position: relative;
  left: 60px;
  bottom: 55px;
  
}
.cuadrado {
  width: 150px;
  height: 10px;
  background: #efd240;
  margin-left: 53px;
  margin-top: 10px;
}
.section-img img{
  position: relative;
  left: 100%;
  bottom: 345px;
  width: 733px;
  height: 388px;
}
.contacto img {
  width: 100%;
  height: 503px;
  position: relative;
  bottom: 80px;
}
.contacto #cuadrado-contacto {
  width: 100%;
  height: 503px;
  top: 1198px;
  position: absolute;
  background: #598f8f;
  opacity: 0.9;
}

.contacto h4 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 19px;
  color: #ffffff;
  margin: 0px;  
  position: relative;
  bottom: 500px;
  margin-left: 50px;
}
.contacto p {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 15px;
  position: relative;
  bottom: 530px;
  color: #ffffff;

}
.contacto input {
  border: 0px;
  border-radius: 5px;
  background: #e5f5f7;
  outline: none;
  width: 150px;
  height: 25px;
  position: relative;
  bottom: 50px;
  margin-left: 50px;
}
.contacto input#Nombre {
  position: relative;
  bottom: 520px;
}
.contacto input#apellido {
  position: relative;
  right: 40px;
  bottom: 520px;
}
.contacto input#telefono {
  position: relative;
  bottom: 490px;
  right: 409px;
}
.contacto input#email {
  position: relative;
  bottom: 490px;
  right: 449px;
}
.contacto input#cuentanos {
  position: absolute;
  top: 1420px;
  right: 916px;
  width: 315px;
  height: 120px;
}
#cuentanos::-webkit-input-placeholder {
  text-align: start;
  position: relative;
  bottom: 50px; 
}
.contacto input#submit {
  position: relative;
  bottom: 320px;
  right: 820px;
  background: #efd240;
  height: 30px;
}
</style>
