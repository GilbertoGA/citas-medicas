<template>
  <NavBar></NavBar>
  <div>
    <div class="col-md-6 offset-md-3 mt-5">
      <br/>
      <h1>Asignación De Paciente</h1>
      <form v-on:submit.prevent="processAddPaciente">
        <!--        lista de pacientes-->
        <div class="form-group">
          <label for="InputUsername">Paciente</label>
          <select
              v-model="asignacionPaciente.id_paciente"
              class="form-control"
              required="required"
          >
            <option v-for="paciente in pacientes" :value="paciente.id" :key="paciente.id">
              {{ paciente.id_usuario.nombre + " " + paciente.id_usuario.apellido }}
            </option>
          </select>
        </div>

        <!--        lista de familiares-->
        <div class="form-group">
          <label for="InputUsername">Familiar</label>
          <select
              v-model="asignacionPaciente.id_familiar"
              class="form-control"
              required="required"
          >
            <option v-for="familiar in familiares" :value="familiar.id" :key="familiar.id">
              {{ familiar.id_usuario.nombre + " " + familiar.id_usuario.apellido }}
            </option>
          </select>
        </div>

        <!--        lista de medicos-->
        <div class="form-group">
          <label for="InputUsername">Medico</label>
          <select
              v-model="asignacionPaciente.id_personal"
              class="form-control"
              required="required"
          >
            <option v-for="personal in personales" :value="personal.id" :key="personal.id">
              {{ personal.id_usuario.nombre + " " + personal.id_usuario.apellido }}
            </option>
          </select>
        </div>
        <hr>
        <button type="submit" class="btn btn-primary">Registrar</button>
      </form>
    </div>
  </div>


</template>

<script>
import NavBar from "@/components/NavBar";
import axios from "axios";

export default {
  name: "AsignacionPaciente",
  components: {NavBar},
  data: function () {
    return {
      asignacionPaciente: {
        id_paciente: "",
        id_familiar: "",
        id_personal: "",
      },

      pacientes: [],
      paciente: {
        id: "",
        id_usuario: {
          apellido: "",
          nombre: "",
        },
      },

      familiares: [],
      familiar: {
        id: "",
        id_usuario: {
          apellido: "",
          nombre: "",
        },
      },

      personales: [],
      personal: {
        id: "",
        id_usuario: {
          apellido: "",
          nombre: "",
        },
      },
    }
  },
  created() {
    // obtener lista de pacientes desde backend
    axios.get(
        'https://drhouse-be.herokuapp.com/pacientes/'
    ).then(res => {
      this.pacientes = res.data;
      console.log(this.pacientes);
    }).catch(err => {
      console.log(err);
    })

    // obtener lista de faimliares desde backend
    axios.get(
        'https://drhouse-be.herokuapp.com/familiares/'
    ).then(res => {
      this.familiares = res.data;
      console.log(this.familiares);
    }).catch(err => {
      console.log(err);
    })

    // obtener lista de medicos desde backend
    axios.get(
        'https://drhouse-be.herokuapp.com/personal-salud-list/'
    ).then(res => {
      this.personales = res.data;
      console.log(this.personales);
    }).catch(err => {
      console.log(err);
    })
  },
}
</script>

<style scoped>

</style>