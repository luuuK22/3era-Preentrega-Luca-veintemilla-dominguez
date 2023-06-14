from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def home(request):
    return render(request, "appdeprueba/inicio.html")

def cursos(request):
    return render(request, "appdeprueba/cursos.html")

def profesores(request):
    return render(request, "appdeprueba/Profesor.html")

def alumnos(request):
    return  render(request, "appdeprueba/Estudiante.html")

def entregables(request):
    return render(request, "appdeprueba/entregable.html")

def iniciar_sesion(request):
    return render(request, "appdeprueba/iniciar_sesion.html")