from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def home(request):
    return render(request, "appdeprueba/index.html")

def cursos(request):
    return render(request, "cursos.html")

def profesores(request):
    return HttpResponse("vista de profes")

def alumnos(request):
    return HttpResponse("vista de alumnos")