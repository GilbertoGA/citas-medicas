<template>
  <NavBar></NavBar>

  <div>
    <div>
      <h1>Asignación De Pacientes</h1>
      <table class="table table-striped">
        <thead>
        <tr>
          <th scope="col">Nombre Paciente</th>
          <th scope="col">EPS</th>
          <th scope="col">Tipo documento</th>
          <th scope="col">Identificacion</th>
          <th scope="col">Fecha Nacimiento</th>
          <th scope="col">Medico Asignado</th>
          <th scope="col">Familiar Asignado</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="asignacion in asignaciones" :key="asignacion.id">
          <td>{{ asignacion.id_paciente.id_usuario.nombre + " " + asignacion.id_paciente.id_usuario.apellido }}</td>
          <td>{{ asignacion.id_paciente.eps }}</td>
          <td>{{ asignacion.id_paciente.id_usuario.tipo_documento }}</td>
          <td>{{ asignacion.id_paciente.id_usuario.numero_documento }}</td>
          <td>{{ asignacion.id_paciente.fecha_nacimiento}}</td>
          <td>{{ asignacion.id_personal.id_usuario.nombre + " " + asignacion.id_personal.id_usuario.apellido }}</td>
          <td>{{ asignacion.id_personal.id_usuario.nombre }}</td>
        </tr>
        </tbody>
      </table>
      <button v-on:submit.prevent="actualizar" type="submit" class="btn btn-primary">Actualizar</button><hr>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import NavBar from "@/components/NavBar";

export default {
  name: "TablaAsignacion",
  components: {NavBar},

  data: function () {
    return {
      asignaciones: [],
      asignacion: {
        id_paciente: {
          id_usuario: {
            nombre: '',
            apellido: '',
            numero_documento: '',
            tipo_documento: 'AAAA-mm-dd',
          },
          fecha_nacimiento: '',
          eps: '',

        },
        id_familiar: {
          id_usuario: {
            nombre: '',
            apellido: ''
          },
          parentesco: '',
        },

        id_personal: {
          id_usuario: {
            nombre: '',
            apellido: ''
          },
        },
      },
    }
  },
  created() {
    // obtener lista de asginaciones desde backend
    axios.get(
        'https://drhouse-be.herokuapp.com/asignaciones-paciente/'
    ).then(res => {
          // obtener el nombre, apellido,eps del paciente, nombre parentesco del familiar y nombre apellido del personal
          this.asignaciones = res.data.map(asignacion => {
            return {
              id: asignacion.id,
              id_familiar: {
                id_usuario: {
                  nombre: asignacion.id_familiar.id_usuario.nombre,
                  apellido: asignacion.id_familiar.id_usuario.apellido,
                  parentesco: asignacion.id_familiar.parentesco,
                },
              },
              id_paciente: {
                id_usuario: {
                  nombre: asignacion.id_paciente.id_usuario.nombre,
                  apellido: asignacion.id_paciente.id_usuario.apellido,
                  numero_documento: asignacion.id_paciente.id_usuario.numero_documento,
                  tipo_documento: asignacion.id_paciente.id_usuario.tipo_documento,
                },
                fecha_nacimiento: asignacion.id_paciente.fecha_nacimiento,
                eps: asignacion.id_paciente.eps,
              },
              id_personal: {
                id_usuario: {
                  nombre: asignacion.id_personal.id_usuario.nombre,
                  apellido: asignacion.id_personal.id_usuario.apellido,
                },
              },
            }
          })
          console.log(this.asignaciones);
        },
    );
  },
  methods:{
    actualizar: function (){
      this.$router.push({name: 'AsignacionPaciente'})
    }
  }
}

</script>

<style scoped>
/*centrar un boton */
.btn {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
/*centrar titulo h1 con bordes de 5px*/
h1 {
  text-align: center;
  border: 5px ;
  padding: 10px;
}
</style>