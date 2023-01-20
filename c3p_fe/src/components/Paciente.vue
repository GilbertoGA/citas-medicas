<template>
  <NavBar></NavBar>

  <div class="col-md-6 offset-md-3 mt-5">
    <br/>
    <h1>Registrar Paciente</h1>
    <form v-on:submit.prevent="processAddPaciente">
      <div class="form-group">
        <label for="InputUsername">Username</label>
        <select
            v-model="paciente.id_usuario"
            class="form-control"
            required="required"
        >
          <option v-for="user in usuarios" :value="user.id" :key="user.id">
            {{ user.username }}
          </option>
        </select>
      </div>

      <!--      fecha de nacimiento-->
      <div class="form-group">
        <label for="InputFechaNacimiento">Fecha de Nacimiento</label>
        <input
            type="date"
            v-model="paciente.fecha_nacimiento"
            class="form-control"
            id="fecha_nacimiento"
            placeholder="Fecha de Nacimiento"
            required="required"
        />
      </div>

      <!--      eps-->
      <div class="form-group">
        <label for="InputUsername">EPS</label>
        <input
            type="text"
            v-model="paciente.eps"
            class="form-control"
            id="eps"
            placeholder="EPS"
            required="required"
        />
      </div>

      <!--      rh-->
      <div class="form-group">
        <label for="InputUsername">RH</label>
        <select
            class="form-control"
            id="rh"
            v-model="paciente.rh"
            required="required"
        >
          <option value="O+">O+</option>
          <option value="O-">O-</option>
          <option value="A+">A+</option>
          <option value="A-">A-</option>
          <option value="B+">B+</option>
          <option value="B-">B-</option>
          <option value="AB+">AB+</option>
          <option value="AB-">AB-</option>
        </select>
      </div>

      <!--      coordenadas-->
      <div class="form-group">
        <label for="InputUsername">Coordenadas</label>
        <input
            type="text"
            v-model="paciente.coordenadas"
            class="form-control"
            id="coordenadas"
            placeholder="2.849293 , 30.293822"
            required="required"
        />
      </div>
      <hr/>
      <button type="submit" class="btn btn-primary">Registrar Paciente</button>
    </form>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";
import NavBar from "@/components/NavBar";

export default {
  name: "PacienteRegistro",
  components: {NavBar},

  data: function () {
    return {
      paciente: {
        id_usuario: "",
        fecha_nacimiento: '',
        eps: '',
        rh: 'O+',
        coordenadas: '',
      },
      usuarios: [],
      personal_salud: {
        username: "",
        id: "",
      }
    }
  },
  created() {
    axios.get('https://drhouse-be.herokuapp.com/users/')
        .then(res => {
          this.usuarios = res.data;
          console.log(this.usuarios);

        })
  },
  methods: {
    processAddPaciente: function () {
      axios.post(
          'https://drhouse-be.herokuapp.com/paciente/',
          this.paciente,
          {headers: {}}
      ).then(res => {
        console.log(res);
        alert("Paciente registrado");
        this.$router.push({name: 'homeUser'});
      }).catch((error) => {
        console.log(error);
      });
    }
  }
}

</script>
<style scoped>

</style>