<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a v-on:click="home" class="nav-link" href="#">Inicio</a>
          </li>
          <li class="nav-item">
            <a v-on:click="paciente" class="nav-link" href="#">Crear Paciente</a>
          </li>
          <li class="nav-item">
            <a v-on:click="personalSalud" class="nav-link" href="#">Crear Medico</a>
          </li>
          <li class="nav-item">
            <a v-on:click="asignacionPaciente" class="nav-link" href="#">Asignar Paciente</a>
          </li>
          <li class="nav-item">
            <a v-on:click="tablaAsignacion" class="nav-link" href="#">Tabla De Asignación Paciente</a>
          </li>
          <li v-on:click="logOut" class="nav-item">
            <a class="nav-link" href="#">Cerrar Sesion</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
    tablaAsignacion: function () {
      this.$router.push({name: "tableAsignacion"})
    },
    personalSalud: function () {
      this.$router.push({name: "personalSalud"})
    },
    paciente: function () {
      this.$router.push({name: "paciente"})
    },
    asignacionPaciente: function () {
      this.$router.push({name: "asignacionPaciente"})
    },
    home: function () {
      this.$router.push({name: "homeUser"})
    },
    logOut: function(){
      localStorage.clear();
      alert("Sesion Cerrada");
      localStorage.setItem("isAuth",false);
      this.$router.push({name: "root"})
    },
  }
}
</script>

<style scoped>

</style>