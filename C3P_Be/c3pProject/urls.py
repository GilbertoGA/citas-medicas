"""c3pProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from c3pAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    # Usuarios
    path('user/', views.UsuarioCreateView.as_view()),
    path('user/<int:pk>/', views.UsuarioDetailView.as_view()),
    path('users/', views.UsuarioListView.as_view()),
    # Pacientes
    path('paciente/', views.PacienteCreateView.as_view()),
    path('paciente/<int:pk>/', views.PacienteDetailView.as_view()),
    path('pacientes/', views.PacienteListView.as_view()),
    # Personal_Salud
    path('personal-salud/', views.Personal_SaludCreateView.as_view()),
    path('personal-salud-list/', views.Personal_SaludListView.as_view()),
    path('personal-salud/<int:pk>/', views.Personal_SaludDetailView.as_view()),
    # Familiar
    path('familiar/', views.FamiliarCreateView.as_view()),
    path('familiares/', views.FamiliarListView.as_view()),
    # Asignacion_Paciente
    path('asignacion-paciente/', views.Asignacion_PacienteCreateView.as_view()),
    path('asignaciones-paciente/', views.Asignacion_PacienteListView.as_view()),
    path('asignacion-paciente/<int:id_paciente>/', views.Asignacion_PacienteDetailView.as_view()),
    # Signos_Vitales
    path('signos-vitales/',views.Signos_VitalesCreateView.as_view()),
    # Historial_Signos
    path('historial-signos/',views.Historial_SignosCreateView.as_view()),
    path('historial-signos/<int:id_paciente>/',views.Historial_SignosDetailView.as_view()),
    #
    path('sugerencia/',views.SugerenciaCreateView.as_view()),
    path('sugerencia/<int:id_historial_signos>/',views.SugerenciaDetailView.as_view())

]
