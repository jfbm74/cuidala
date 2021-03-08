<template>

<!-- Registro -->
<div class="registro">
    <div class="caja">
        <p class="title">
            Elige una opción
        </p>
    </div>
  <div class="cuidador">
    <h3>
      Necesito un <br>Cuidador
    </h3>
    <p>
      Inicie su búsqueda gratuita de cuidador en su área
    </p>
    <input type="submit" value="Encuentra Cuidador">
  </div>
  <div class="job">
    <h3>
      Quiero un trabajo de <br>cuidador
    </h3>
    <p>
      Crea un perfil y busca trabajo<br><br>
    </p>
    <a href="https://articulo.mercadolibre.com.co/MCO-603729660-monitor-lg-ips-de-29-full-hd-75hz-hdmi-displayport-29wn600-_JM?searchVariation=73991616153#searchVariation=73991616153&position=22&type=item&tracking_id=02aa70d5-6b1d-48d5-a271-a69aa58d3fbf"><input type="submit" value="Encontrar trabajos"></a>
  </div>
</div>
<!-- end Registro -->

</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* Registro */
.caja {
    
    width: 100%;
    height: 100px;
}
.registro .title {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 24px;
  text-align: center;
  position: absolute;
  top: 100px;
  left: 540px;
}
.cuidador {
  margin: 100px 0 0 250px;
  width: 350px;
  height: 191px;
  border: solid 1px;
}
h3 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 22px;
  text-align: center;
  padding: 10px;
  margin: 0px;
}
p {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
  margin: 0;
  padding: 10px;
  text-align: center;
}
input {
  width: 210px;
  height: 40px;
  position: relative;
  left: 0px;
  top: 10px;
  border-radius: 15px;
  background-color: #28808a;
  border: 0;
  outline: none;
  font-size: 16px;
  color: #fff;
  font-family: Arial, Helvetica, sans-serif; 
}
input:hover {
  background-color: #50868d;
  transition: background-color .5s;
  cursor: pointer;
}

.job {
  margin: 100px 0 0 250px;
  width: 350px;
  height: 191px;
  position: relative;
  left: 400px;
  bottom: 293px;
  border: solid 1px;
}
/* end Registro */

</style>
