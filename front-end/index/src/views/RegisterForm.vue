<template>
  <div class="RegisterForm">
    <!-- Start Contact Form Area -->
    <section class="contact__form__area ptb--100 bg-white">
      <div class="container">
        <div class="row">
          <div class="col-md-12 col-lg-12 col-sm-12 col-xs-12">
            <div class="contact-form-wrap bg-cat-3">
              <h2 class="contact__title">Cuéntanos sobre ti</h2>
              <form id="contact-form" action="mail.php" method="post">
                <div class="single-contact-form">
                  <!-- <div class="contact-box">
                      <label for="">Nombres*</label>
                      <input type="text" name="name" class="form-control">
                      <label for="">Apellidos*</label>
                      <input type="text" name="lastname" class="form-control">
                  </div> -->
                  <label for="">Nombres*</label>
                  <input type="text" name="name" class="form-control" required v-model.trim="form.first_name">
                  <br>
                  <label for="">Apellidos*</label>
                  <input type="text" name="lastname" class="form-control" required v-model.trim="form.last_name">
                  <br>
                  <label for="">Cédula*</label>
                  <input type="tel" name="cedula" class="form-control" required v-model.trim="form.legal_id">
                  <br>
                  <label for="">Email*</label>
                  <input type="email" name="email" class="form-control" v-model.trim="form.email">
                  <br>
                  <label for="">Passowrd*</label>
                  <input type="password" name="pwd" class="form-control" v-model.trim="form.password">
                  <br>
                  <label for="menu">Ciudad</label>
                  <br><select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example" id="menu" name="menu" v-model.trim="form.location_id"> <!-- Consumir la API -->
                    <option selected>Seleccione una opción</option>
                    <option value="1">Cali</option>
                    <option value="2">Bogotá</option>
                    <option value="3">Medellín</option>
                    <option value="4">Barranquilla</option>
                  </select><br>
                  <label for="">Dirección</label>
                  <input type="text" name="address" class="form-control" v-model.trim="form.adress">
                </div>
                <br>
                <label for="">Celular</label>
                <input type="tel" name="phone" class="form-control" v-model.trim="form.phone">
                <div class="single-contact-form">
                    <label for="">Subir foto</label>
                    <input class="form-control form-control-sm" type="file" name="foto">
                </div>
                <div class="single-contact-form">
                  <div class="contact-box message"></div>
                </div>
                <div class="contact-btn">
                  <button type="submit" class="bst__btn btn--theme__color">REGÍSTRATE</button>
                </div>
              </form>
            </div>
            <div class="form-output">
              <p class="form-messege"></p>
            </div>
          </div>
        </div>
      </div>            
    </section>
    <!-- End Contact Form Area -->
    <Footer/>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'
import Footer from '@/components/Footer.vue'

export default {
  name: 'RegisterForm',
  components: {
    Footer
  },
  data () {
      return {
          form: {
              first_name: '',
              last_name: '',
              legal_id: '',
              email: '',
              password: '',
              caregiver: true,
              patient: false,
              adress: '',
              phone: '',
              location_id: '',
          }

      }
  },
  methods: {
      onSubmit (evt) {
          evt.preventDefault()
          const path = 'http://localhost:8000/api/v1/user/'
          axios.post(path, this.form).then((response) => {
              this.form.first_name = response.data.first_name
              this.form.last_name = response.data.last_name
              this.form.legal_id = response.data.legal_id
              this.form.email = response.data.email
              this.form.password = response.data.password
              this.form.caregiver = response.data.caregiver
              this.form.patient = response.data.patient
              this.form.adress = response.data.adress
              this.form.phone = response.data.phone
              this.form.location_id = response.data.location_id

              swal("Usuario creado exitosamente", "", "success")

          })
          .catch((error) => {
              swal("No se pudo crear usuario", "", "error")
          })
      }
  },
  created() {

  }
}
</script>

<style scoped>
.ptb--100 {
  padding: 30px;
}
</style>