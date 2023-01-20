import {createRouter, createWebHistory} from 'vue-router'
// import App from './App.vue'
import LogIn from "@/components/LogIn";
import SignUp from "@/components/SignUp";
import Home from "@/components/Home";
import PersonalSalud from "@/components/PersonalSalud";
import Paciente from "@/components/Paciente";
import AsignacionPaciente from "@/components/AsignacionPaciente";
import TablaAsignacion from "@/components/TablaAsignacion";

const routes = [
    {path: '/', name: 'root', component: LogIn},
    {path: '/user/logIn', name: 'logIn', component: LogIn},
    {path: '/user/signUp', name: 'signUp', component: SignUp},
    {path: '/user/home', name: 'homeUser', component: Home},
    {path: '/user/tableAsignacion', name: 'tableAsignacion', component: TablaAsignacion},
    {path: '/user/personalSalud', name: 'personalSalud', component: PersonalSalud},
    {path: '/user/paciente', name: 'paciente', component: Paciente},
    {path: '/user/asignacionPaciente', name: 'asignacionPaciente', component: AsignacionPaciente},
]

const router = createRouter({
    history: createWebHistory(), routes,
})

export default router