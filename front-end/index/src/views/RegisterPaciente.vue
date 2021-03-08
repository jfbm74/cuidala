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
      Dirección
      <br><input type="text" id="direccion" name="direccion" placeholder="Dirección"><br>
      Preferencias de trabajo
      <br><select name="trabajo"><br>
      <option value="0">...</option>
      <option value="1">Tiempo completo</option>
      <option value="2">Medio tiempo</option>
      <option value="3">Por hora</option>
      </select><br>
      Subir foto
      <br><input type="text" id="foto" name="foto" placeholder="Subir foto"><br>
      <br><input type="submit" id="submit" value="Guardar">
    </p>
    </form>
  </div>
  <!-- end contacto -->
</template>

<script>
export default {
  name: 'RegisterPaciente'
}
</script>