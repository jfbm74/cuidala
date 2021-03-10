<template>
  <!-- Contacto -->
  <div class="registerPaciente">
    <form @submit="onSubmit">
    <h4>Cuéntanos acerca de ti</h4>
    <p>
      <label for="nombre">Nombre<abbr title="required" aria-label="required">*</abbr></label>
      <br><input type="text" id="nombre" name="Nombre" placeholder="Nombre" required v-model.trim="form.first_name"><br>
      <label for="apellido">Apellido*</label>
      <br><input type="text" id="apellido" name="apellido" placeholder="Apellido" required v-model.trim="form.last_name"><br>
      <label for="cedula">Cédula*</label>
      <br><input type="tel" id="cedula" name="cedula" placeholder="Cédula" required v-model.trim="form.legal_id"><br>
      Género
      <br><input type="radio" id="mujer" name="mujer">
          <label for="mujer">Mujer</label>
          <input type="radio" id="hombre" name="hombre">
          <label for="hombre">Hombre</label>
      <br>
      <label for="fecha">Fecha de nacimiento*</label>
      <br><input type="date" id="fecha" name="fecha"><br>
      <label for="menu">Ciudad</label>
      <br><select id="menu" name="menu" v-model.trim="form.location_id"> <!-- Consumir la API -->
      <option value="0">...</option>
      <option value="1">Cali</option>
      <option value="2">Bogotá</option>
      <option value="3">Medellín</option>
      <option value="4">Barranquilla</option>
      </select><br>
      <label for="celular">Celular</label>
      <br><input type="tel" id="celular" name="celular" v-model.trim="form.phone"><br>
      <label for="email">Correo electrónico</label>
      <br><input type="email" id="email" name="email" v-model.trim="form.email"><br>
      <label for="vemail">Verifica tu correo electrónico</label>
      <br><input type="email" id="vemail" name="email"><br>
      <label for="password">Password</label>
      <br><input type="password" id="password" name="password" placeholder="Contraseña" v-model.trim="form.password"><br>
      <label for="direccion">Dirección</label>
      <br><input type="text" id="direccion" name="direccion" v-model.trim="form.adress"><br>
      Disponibilidad / Nº de horas
      <br><input type="time" id="hora" name="hora"><br>
      <label for="trabajo">Preferencias de trabajo</label>
      <br><select id="trabajo" name="trabajo"><!-- Consumir la API -->
      <option value="0">...</option>
      <option value="1">Tiempo completo</option>
      <option value="2">Medio tiempo</option>
      <option value="3">Por hora</option>
      </select>
      <br>
      <label for="servicio">Servicios</label>
      <br><select id="servicio" name="servicio"><!-- Consumir la API -->
      <option value="0">...</option>
      <option value="1">Suministro de medicamentos</option>
      <option value="2">Aseo del paciente</option>
      <option value="3">Cuidado integral</option>
      </select><br>
      <label for="educacion">Educación</label>
      <br><select id="educacion" name="educacion"><!-- Consumir la API -->
      <option value="0">...</option>
      <option value="1">Primaria</option>
      <option value="2">Secundaria</option>
      <option value="3">Técnico</option>
      <option value="4">Tecnológico</option>
      <option value="5">Universitario</option>
      <option value="6">No tiene</option>
      </select><br>
      <label for="habilidades">Habilidades</label>
      <br><select id="habilidades" name="habilidades"><!-- Consumir la API -->
      <option value="0">...</option>
      <option value="1">Inyectología</option>
      <option value="2">Curaciones</option>
      <option value="3">Toma de signos vitales</option>
      <option value="4">Suministro de alimentos</option>
      </select><br>
      <label for="experiencia">Experiencia</label>
      <br><select id="experiencia" name="experiencia"><!-- Consumir la API -->
      <option value="0">...</option>
      <option value="1">0 - 2 años</option>
      <option value="2">2 - 4 años</option>
      <option value="3">4 - 6 años</option>
      </select><br>
      <label for="file">Subir foto</label>
      <input type="file" name="file" id="file" accept="image/*">
      </p>
      <input type="hidden" id="timestamp" name="timestamp" value="1286705410">
      <br><button type="submit">Registrar</button>
    
    </form>
  </div>
  <!-- end contacto -->
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'

export default {
  name: 'RegisterForm',
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