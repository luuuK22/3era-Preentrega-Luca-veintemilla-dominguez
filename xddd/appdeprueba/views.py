from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("vista de inicio")

def cursos(request):
    return HttpResponse("vista cursos")

def profesores(request):
    return HttpResponse("vista de profes")

def alumnos(request):
    return HttpResponse("vista de alumnos")