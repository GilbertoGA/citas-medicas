<template>
  <NavBar></NavBar>

  <div class="col-md-6 offset-md-3 mt-5">
    <br/>
    <h1>Registrar Personal De Salud</h1>
    <form v-on:submit.prevent="processAddDoctor">
      <div class="form-group">
        <label for="InputUsername">Username</label>
        <select v-model="personal_salud.id_usuario" class="form-control">
          <option v-for="user in usuarios" :value="user.id" :key="user.id">
            {{ user.nombre + " " + user.apellido }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="InputPassword">Rol</label>
        <select
            name="rol"
            v-model="personal_salud.id_rol"
            class="form-control"
            required="required"
        >
          <option selected value="1">Medico</option>
          <option value="2">Enfermero</option>
        </select>
      </div>
      <hr/>
      <button type="submit" class="btn btn-primary">Registrar Personal</button>
    </form>
  </div>


</template>

<script>
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import NavBar from "@/components/NavBar";

// import usuario from "@vue/cli-service/lib/PluginAPI";

export default {
  name: "PersonalSalud",
  components: {NavBar},
  data: function () {
    return {
      personal_salud: {
        id_usuario: "",
        id_rol: "1",
      },
      usuarios: [],
      usuario: {
        username: "",
        id: "",
      },
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
    processAddDoctor: function () {
      axios.post(
          'https://drhouse-be.herokuapp.com/personal-salud/',
          this.personal_salud,
          {headers: {}}
      ).then((result) => {
        console.log(result);
        alert("Personal de salud creado");
        this.$router.push({name: 'homeUser'});
        // this.$router.push("/root");
      }).catch((error) => {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>

</style>