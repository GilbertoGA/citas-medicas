<template>

  <NavBar></NavBar>
  <!--  mensaje de bienvenida para usaurio-->
  <!--  <div>-->
  <!--    <div class="col-md-9s offset-md-1 mt-5">-->
  <!--      <h1 class="text-center">Bienvenido {{ this.username }} </h1>-->
  <!--      &lt;!&ndash;      insertar imagen en un div&ndash;&gt;-->
  <!--      <div class="text-center">-->
  <!--        <img src="https://source.unsplash.com/P8bsrm8KbM0" alt="ups" width="900" height="300">-->
  <!--      </div>-->

  <!--      <p>-->
  <!--        Esta es la pagina principal de la aplicacion, aqui podra crear pacientes, medicos y asignar pacientes a medicos.-->
  <!--        <br>-->
  <!--        Elaborada por el grupo 6 MINTIC 2022-->
  <!--      </p>-->
  <!--    </div>-->
  <!--  </div>-->
  <!--nombre del usuario con imagen al lado y un parrafo pantalla completa-->
  <div class="container">
    <div class="row">
      <!--      centrado-->
      <div class="bd-masthead mb-3" id="content">
        <div class="container-xxl bd-gutter">
          <div class="col-md-8 mx-auto text-center">
            <img src="https://source.unsplash.com/fy8WmFBIaRs" width="350" height="350" alt="Medico"
                 class="d-block mx-auto mb-3">
            <h1 class="mb-3 fw-semibold">Bienvenido {{ this.username }} </h1>
            <p class="lead mb-4">
              Este es el inicio de la aplicacion, aqui podra crear pacientes, medicos y asignar pacientes a medicos. Con el
              fin de llevar un control de la salud de los pacientes.
              <br>
<!--              texto en negrilla-->
              <strong>Elaborada por el grupo 6 MINTIC 2022</strong>
            </p>
            <div class="d-flex flex-column flex-lg-row align-items-md-stretch justify-content-md-center gap-3 mb-4">
              <div class="d-inline-block v-align-middle fs-5">
                <div class="highlight">
                  <pre tabindex="0" class="chroma"><code class="language-sh" data-lang="sh"><span class="line"><span
                      class="cl"></span></span></code></pre>
                </div>
              </div>
              <a href="/docs/5.2/getting-started/introduction/"
                 class="btn btn-lg bd-btn-lg btn-bd-primary d-flex align-items-center justify-content-center fw-semibold"
                 onclick="ga('send', 'event', 'Jumbotron actions', 'Get started', 'Get started');">
                <svg class="bi me-2" aria-hidden="true">
                  <use xlink:href="#book-half"></use>
                </svg>
<!--                Read the docs-->
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
import NavBar from "@/components/NavBar";

export default {
  name: "HomeUser",
  components: {NavBar},

  data: function () {
    return {
      username: localStorage.getItem("username")
    }
  },
  methods: {
    "tablaAsignacion": function () {
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
    }
  },
}
</script>
<style scoped>
/*centrar nombre y hacer en forma de tarjeta */
h1 {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  color: #000000;
  background-color: #ffffff;
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
}
/*centrar la imagen*/
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  margin: 20px;
}
</style>