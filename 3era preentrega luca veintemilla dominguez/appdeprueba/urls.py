from django.urls import path

from appdeprueba import views



urlpatterns = [
  
    
    path("inicio",views.home,name="inicio"),
    path("cursos/",views.cursos, name="Cursos"),
    path("alumnos/",views.alumnos,name="Alumnos"),
    path("profes/",views.profesores,name="Profes"),
    path("entregables/",views.entregables,name="Entregables"),
    path("Iniciar_sesion/",views.iniciar_sesion,name="Iniciar sesion")
    

]