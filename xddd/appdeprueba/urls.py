from django.urls import path

from appdeprueba import views



urlpatterns = [
  
    
    path("",views.home),
    path("cursos/",views.cursos),
    path("alumnos/",views.alumnos),
    path("profes/",views.profesores)

]