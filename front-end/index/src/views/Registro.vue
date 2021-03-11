<template>

<!-- Registro -->
  <div class="slider__container slider__full--width">
    <div class="slider__activation__wrap slider-activetion-wrap control__style--left owl-theme">
      <div class="slider">
        <div class="container">
          <div class="row">
            <div class="col-md-12 col-sm-12 col-xs-12 col-lg-12">
              <div class="inner">
                <h2>Elige una opción</h2>
                <div class="service bg-white text-center caja-1">
                  <a class="bst__btn"><router-link to="/registerPaciente">
                  <div class="service__inner">
                  <h2>
                    Necesito un <br>Cuidador
                  </h2>
                  <p>
                    Inicie su búsqueda gratuita de cuidador en su área
                  </p>
                  </div>
                  </router-link></a>
                </div>
                <div class="service bg-white text-center caja-2">
                  <div class="service__inner">
                    <a class="bst__btn"><router-link to="/registerForm">
                      <h2>
                        Quiero un trabajo de <br>Cuidador
                      </h2>
                      <p>
                        Crea un perfil y busca trabajo
                      </p>
                      </router-link></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer/>
  </div>
<!-- end Registro -->
</template>

<script>
import Footer from '@/components/Footer.vue'
export default {
  name: 'Registro',
  components: {
    Footer
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* Registro */
.service {
  width: 300px;
}
.caja {
    
    width: 100%;
    height: 100px;
}
service {
  border-style: solid;
}
h2 {
  text-align: center;
  margin-bottom: 50px;
  margin-top: 50px;
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
  font-size: 14px;
  margin: 0;
  padding: 10px;
  text-align: center;
}

.caja-1 {
  position: absolute;
  left: 55%;
}
.caja-2 {
  position: absolute;
  right: 55%;
}
/* end Registro */

</style>
