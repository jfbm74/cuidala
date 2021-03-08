<template>
  <!-- Contacto -->
  <div class="registerform">
    <form method="get">
    <h4>Cuéntanos acerca de ti</h4>
    <p>
      Nombre*
      <br><input type="text" id="Nombre" name="Nombre" placeholder="Nombre"><br>
      Segundo nombre
      <br><input type="text" id="segundonombre" name="segundo nombre" placeholder="Segundo nombre"><br>
      Apellido*
      <br><input type="text" id="apellido" name="apellido" placeholder="Apellido"><br>
      Género
      <br><input type="radio" id="mujer" name="mujer">Mujer
          <input type="radio" id="hombre" name="hombre">Hombre
      <br>
      Fecha de nacimiento*
      <br><input type="date" id="fecha" name="fecha"><br>
      Ciudad
      <br><select name="menu">
      <option value="0">...</option>
      <option value="1">Cali</option>
      <option value="2">Bogotá</option>
      <option value="3">Medellín</option>
      <option value="4">Barranquilla</option>
      </select><br>
      Celular
      <br><input type="tel" id="celular" name="celular" placeholder="Celular"><br>
      Correo electrónico
      <br><input type="email" id="email" name="email" placeholder="Correo electrónico"><br>
      Disponibilidad / Nº de horas
      <br><input type="time" id="hora" name="hora"><br>
      Preferencias de trabajo
      <br><select name="trabajo">
      <option value="0">...</option>
      <option value="1">Tiempo completo</option>
      <option value="2">Medio tiempo</option>
      <option value="3">Por hora</option>
      </select>
      <br>
      Servicios
      <br><select name="servicio">
      <option value="0">...</option>
      <option value="1">Suministro de medicamentos</option>
      <option value="2">Aseo del paciente</option>
      <option value="3">Cuidado integral</option>
      </select><br>
      Nivel educativo
      <br><select name="educacion">
      <option value="0">...</option>
      <option value="1">Primaria</option>
      <option value="2">Secundaria</option>
      <option value="3">Técnico</option>
      <option value="4">Tecnológico</option>
      <option value="5">Universitario</option>
      <option value="6">No tiene</option>
      </select><br>
      Habilidades
      <br><select name="habilidades">
      <option value="0">...</option>
      <option value="1">Inyectología</option>
      <option value="2">Curaciones</option>
      <option value="3">Toma de signos vitales</option>
      <option value="4">Suministro de alimentos</option>
      </select><br>
      Experiencia
      <br><select name="experiencia">
      <option value="0">...</option>
      <option value="1">0 - 2 años</option>
      <option value="2">2 - 4 años</option>
      <option value="3">4 - 6 años</option>
      </select><br>
      Subir foto
      <br><input type="text" id="foto" name="foto" placeholder="Subir foto"><br>
      </p>
      <br><input type="submit" id="submit" value="Guardar">
    
    </form>
  </div>
  <!-- end contacto -->
</template>

<script>
export default {
  name: 'RegisterForm',
}
</script>