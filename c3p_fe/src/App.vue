<template>
  <div id="app" class="app">
    <div class="main-component">
      <router-view
          v-on:completedLogIn="completedLogIn"
          v-on:completedSignUp="completedSignUp"
      >
      </router-view>
    </div>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
export default {
  name: 'App',
  data: function () {
    return {
      is_auth: false,
    }
  },

  methods: {
    completedLogIn: function(data){
      localStorage.setItem("isAuth",true);
      localStorage.setItem("username",data.username);
      localStorage.setItem("token_access",data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticacion Exitosa");
      this.verifyAuth();
    },
    verifyAuth: function(){
      this.is_auth = localStorage.getItem("isAuth") || false;
      if(this.is_auth === false){
        console.log("No estas autenticado");
        this.$router.push({name: "root"});
      }else{
        this.$router.push({name: "homeUser"});
      }
    },
    completedSignUp: function(data){
      alert("Registro de usuario");
      this.completedLogIn(data);
    }
  },

  created: function () {
  },


}
</script>

<style>

.form-white.input-group>.form-control:focus {
  border-color: #fff;
  box-shadow: inset 0 0 0 1px #fff;
}

.navbar-dark .navbar-nav .nav-link {
  color: #fff;
}

.navbar-dark .navbar-nav .nav-link:hover,
.navbar-dark .navbar-nav .nav-link:focus {
  color: rgba(255, 255, 255, 0.75);
}
</style>
