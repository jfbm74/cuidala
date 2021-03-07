<template>
    <div class="footer">
      <h3>CUIDA.LA</h3>
      <img class="face" src="data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjUxMnB0IiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgd2lkdGg9IjUxMnB0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im00ODMuNzM4MjgxIDBoLTQ1NS41Yy0xNS41OTc2NTYuMDA3ODEyNS0yOC4yNDIxODcyNSAxMi42NjAxNTYtMjguMjM4MjgxIDI4LjI2MTcxOXY0NTUuNWMuMDA3ODEyNSAxNS41OTc2NTYgMTIuNjYwMTU2IDI4LjI0MjE4NyAyOC4yNjE3MTkgMjguMjM4MjgxaDQ1NS40NzY1NjJjMTUuNjA1NDY5LjAwMzkwNiAyOC4yNTc4MTMtMTIuNjQ0NTMxIDI4LjI2MTcxOS0yOC4yNSAwLS4wMDM5MDYgMC0uMDA3ODEyIDAtLjAxMTcxOXYtNDU1LjVjLS4wMDc4MTItMTUuNTk3NjU2LTEyLjY2MDE1Ni0yOC4yNDIxODcyNS0yOC4yNjE3MTktMjguMjM4Mjgxem0wIDAiIGZpbGw9IiM0MjY3YjIiLz48cGF0aCBkPSJtMzUzLjUgNTEydi0xOThoNjYuNzVsMTAtNzcuNWgtNzYuNzV2LTQ5LjM1OTM3NWMwLTIyLjM4NjcxOSA2LjIxNDg0NC0zNy42NDA2MjUgMzguMzE2NDA2LTM3LjY0MDYyNWg0MC42ODM1OTR2LTY5LjEyODkwNmMtNy4wNzgxMjUtLjk0MTQwNi0zMS4zNjMyODEtMy4wNDY4NzUtNTkuNjIxMDk0LTMuMDQ2ODc1LTU5IDAtOTkuMzc4OTA2IDM2LTk5LjM3ODkwNiAxMDIuMTQwNjI1djU3LjAzNTE1NmgtNjYuNXY3Ny41aDY2LjV2MTk4em0wIDAiIGZpbGw9IiNmZmYiLz48L3N2Zz4=" />
      <img class="insta" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNTEyIDUxMjsiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGxpbmVhckdyYWRpZW50IGlkPSJTVkdJRF8xXyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSItNDYuMDA0MSIgeTE9IjYzNC4xMjA4IiB4Mj0iLTMyLjkzMzQiIHkyPSI2NDcuMTkxNyIgZ3JhZGllbnRUcmFuc2Zvcm09Im1hdHJpeCgzMiAwIDAgLTMyIDE1MTkgMjA3NTcpIj4NCgk8c3RvcCAgb2Zmc2V0PSIwIiBzdHlsZT0ic3RvcC1jb2xvcjojRkZDMTA3Ii8+DQoJPHN0b3AgIG9mZnNldD0iMC41MDciIHN0eWxlPSJzdG9wLWNvbG9yOiNGNDQzMzYiLz4NCgk8c3RvcCAgb2Zmc2V0PSIwLjk5IiBzdHlsZT0ic3RvcC1jb2xvcjojOUMyN0IwIi8+DQo8L2xpbmVhckdyYWRpZW50Pg0KPHBhdGggc3R5bGU9ImZpbGw6dXJsKCNTVkdJRF8xXyk7IiBkPSJNMzUyLDBIMTYwQzcxLjY0OCwwLDAsNzEuNjQ4LDAsMTYwdjE5MmMwLDg4LjM1Miw3MS42NDgsMTYwLDE2MCwxNjBoMTkyDQoJYzg4LjM1MiwwLDE2MC03MS42NDgsMTYwLTE2MFYxNjBDNTEyLDcxLjY0OCw0NDAuMzUyLDAsMzUyLDB6IE00NjQsMzUyYzAsNjEuNzYtNTAuMjQsMTEyLTExMiwxMTJIMTYwYy02MS43NiwwLTExMi01MC4yNC0xMTItMTEyDQoJVjE2MEM0OCw5OC4yNCw5OC4yNCw0OCwxNjAsNDhoMTkyYzYxLjc2LDAsMTEyLDUwLjI0LDExMiwxMTJWMzUyeiIvPg0KPGxpbmVhckdyYWRpZW50IGlkPSJTVkdJRF8yXyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSItNDIuMjk3MSIgeTE9IjYzNy44Mjc5IiB4Mj0iLTM2LjY0MDQiIHkyPSI2NDMuNDg0NiIgZ3JhZGllbnRUcmFuc2Zvcm09Im1hdHJpeCgzMiAwIDAgLTMyIDE1MTkgMjA3NTcpIj4NCgk8c3RvcCAgb2Zmc2V0PSIwIiBzdHlsZT0ic3RvcC1jb2xvcjojRkZDMTA3Ii8+DQoJPHN0b3AgIG9mZnNldD0iMC41MDciIHN0eWxlPSJzdG9wLWNvbG9yOiNGNDQzMzYiLz4NCgk8c3RvcCAgb2Zmc2V0PSIwLjk5IiBzdHlsZT0ic3RvcC1jb2xvcjojOUMyN0IwIi8+DQo8L2xpbmVhckdyYWRpZW50Pg0KPHBhdGggc3R5bGU9ImZpbGw6dXJsKCNTVkdJRF8yXyk7IiBkPSJNMjU2LDEyOGMtNzAuNjg4LDAtMTI4LDU3LjMxMi0xMjgsMTI4czU3LjMxMiwxMjgsMTI4LDEyOHMxMjgtNTcuMzEyLDEyOC0xMjgNCglTMzI2LjY4OCwxMjgsMjU2LDEyOHogTTI1NiwzMzZjLTQ0LjA5NiwwLTgwLTM1LjkwNC04MC04MGMwLTQ0LjEyOCwzNS45MDQtODAsODAtODBzODAsMzUuODcyLDgwLDgwDQoJQzMzNiwzMDAuMDk2LDMwMC4wOTYsMzM2LDI1NiwzMzZ6Ii8+DQo8bGluZWFyR3JhZGllbnQgaWQ9IlNWR0lEXzNfIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9Ii0zNS41NDU2IiB5MT0iNjQ0LjU3OTMiIHgyPSItMzQuNzkxOSIgeTI9IjY0NS4zMzMxIiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KDMyIDAgMCAtMzIgMTUxOSAyMDc1NykiPg0KCTxzdG9wICBvZmZzZXQ9IjAiIHN0eWxlPSJzdG9wLWNvbG9yOiNGRkMxMDciLz4NCgk8c3RvcCAgb2Zmc2V0PSIwLjUwNyIgc3R5bGU9InN0b3AtY29sb3I6I0Y0NDMzNiIvPg0KCTxzdG9wICBvZmZzZXQ9IjAuOTkiIHN0eWxlPSJzdG9wLWNvbG9yOiM5QzI3QjAiLz4NCjwvbGluZWFyR3JhZGllbnQ+DQo8Y2lyY2xlIHN0eWxlPSJmaWxsOnVybCgjU1ZHSURfM18pOyIgY3g9IjM5My42IiBjeT0iMTE4LjQiIHI9IjE3LjA1NiIvPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPC9zdmc+DQo=" />
      <img class="linke" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCINCgkgdmlld0JveD0iMCAwIDM4MiAzODIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDM4MiAzODI7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxwYXRoIHN0eWxlPSJmaWxsOiMwMDc3Qjc7IiBkPSJNMzQ3LjQ0NSwwSDM0LjU1NUMxNS40NzEsMCwwLDE1LjQ3MSwwLDM0LjU1NXYzMTIuODg5QzAsMzY2LjUyOSwxNS40NzEsMzgyLDM0LjU1NSwzODJoMzEyLjg4OQ0KCUMzNjYuNTI5LDM4MiwzODIsMzY2LjUyOSwzODIsMzQ3LjQ0NFYzNC41NTVDMzgyLDE1LjQ3MSwzNjYuNTI5LDAsMzQ3LjQ0NSwweiBNMTE4LjIwNywzMjkuODQ0YzAsNS41NTQtNC41MDIsMTAuMDU2LTEwLjA1NiwxMC4wNTYNCglINjUuMzQ1Yy01LjU1NCwwLTEwLjA1Ni00LjUwMi0xMC4wNTYtMTAuMDU2VjE1MC40MDNjMC01LjU1NCw0LjUwMi0xMC4wNTYsMTAuMDU2LTEwLjA1Nmg0Mi44MDYNCgljNS41NTQsMCwxMC4wNTYsNC41MDIsMTAuMDU2LDEwLjA1NlYzMjkuODQ0eiBNODYuNzQ4LDEyMy40MzJjLTIyLjQ1OSwwLTQwLjY2Ni0xOC4yMDctNDAuNjY2LTQwLjY2NlM2NC4yODksNDIuMSw4Ni43NDgsNDIuMQ0KCXM0MC42NjYsMTguMjA3LDQwLjY2Niw0MC42NjZTMTA5LjIwOCwxMjMuNDMyLDg2Ljc0OCwxMjMuNDMyeiBNMzQxLjkxLDMzMC42NTRjMCw1LjEwNi00LjE0LDkuMjQ2LTkuMjQ2LDkuMjQ2SDI4Ni43Mw0KCWMtNS4xMDYsMC05LjI0Ni00LjE0LTkuMjQ2LTkuMjQ2di04NC4xNjhjMC0xMi41NTYsMy42ODMtNTUuMDIxLTMyLjgxMy01NS4wMjFjLTI4LjMwOSwwLTM0LjA1MSwyOS4wNjYtMzUuMjA0LDQyLjExdjk3LjA3OQ0KCWMwLDUuMTA2LTQuMTM5LDkuMjQ2LTkuMjQ2LDkuMjQ2aC00NC40MjZjLTUuMTA2LDAtOS4yNDYtNC4xNC05LjI0Ni05LjI0NlYxNDkuNTkzYzAtNS4xMDYsNC4xNC05LjI0Niw5LjI0Ni05LjI0Nmg0NC40MjYNCgljNS4xMDYsMCw5LjI0Niw0LjE0LDkuMjQ2LDkuMjQ2djE1LjY1NWMxMC40OTctMTUuNzUzLDI2LjA5Ny0yNy45MTIsNTkuMzEyLTI3LjkxMmM3My41NTIsMCw3My4xMzEsNjguNzE2LDczLjEzMSwxMDYuNDcyDQoJTDM0MS45MSwzMzAuNjU0TDM0MS45MSwzMzAuNjU0eiIvPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPC9zdmc+DQo=" />
      <div class="informacion">
        <h4>Más información</h4>
        <a href="#" class="nosotros">Sobre nosotros</a>
        <a href="#" class="cuidadores">Cuidadores</a>
        <a href="#" class="contacto">Contacto</a>
      </div>
      <div class="direccion">
        <h4>Dirección</h4>
        <p class="cali">Cali - Valle, Colombia</p>
        <p class="email">cuidala@gmail.com</p>
      </div>
      <div class="copy">
        <p>
          CUIDA.LA 2021 / Todos los derechos son reservados
        </p>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
.footer {
  width: 100%;
  background: #4e4e4e;
}
h3 {
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bold;
  font-size: 50px;
  padding: 70px;
  text-align: left;
  color: #fff;
}
.footer img {
  height: 50px;
  float: left;
}
.footer .face {
  margin-left: 70px;
}
.footer .insta {
  margin-left: 20px;
}
.footer .linke {
  margin-left: 20px;
}
.informacion {
  position: relative;
  width: 200px;
  height: 100px;
  left: 400px;
  margin: 0;
}
.informacion h4 {
  width: 400px;
  height: 40px;
  color: #fff;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
  text-align: left;
  position: absolute;
}
.informacion .nosotros {
  position: absolute;
  text-decoration: none;
  color: #fff;
  text-align: left;
  width: 200px;
  top: 40px;
  right: 0px;
}
.informacion .cuidadores {
  text-decoration: none;
  color: #fff;
  width: 200px;
  position: absolute;
  text-align: left;
  top: 70px;
  right: 0;
}
.informacion .contacto {
  text-decoration: none;
  color: #fff;
  width: 200px;
  position: absolute;
  text-align: left;
  top: 100px;
  right: 0;
}
.direccion {
  position: relative;
  width: 400px;
  height: 100px;
  left: 700px;
  bottom: 100px;
  margin: 0;
}
.direccion h4 {
  width: 400px;
  height: 40px;
  color: #fff;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
  text-align: left;
  position: absolute;
}
.direccion .cali {
  color: #fff;
  width: 400px;
  height: 0;
  position: absolute;
  text-align: left;
  top: 40px;
  right: 0;
}
.direccion .email {
  color: #fff;
  width: 400px;
  position: absolute;
  text-align: left;
  top: 70px;
  right: 0;
  height: 0;
}
.copy {
  height: 37px;
  background: #000;
}
.copy p {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 15px;
  font-weight: bold;
  text-align: center;
  color: #fff;
  padding: 10px;
}
</style>