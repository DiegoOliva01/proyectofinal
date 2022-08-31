from django.shortcuts import render
from appdatos import *

# Create your views here.

def inicio(request):
    return render(request,"appdatos/inicio.html")

def individuo(request):
    return render(request,"appdatos/individuo.html")

def vehiculo(request):
    return render(request,"appdatos/vehiculo.html")

def vivienda(request):
    return render(request,"appdatos/vivienda.html")        




def formulario_individuo(request):
    return render(request,"appdatos/formularioindividuo.html")    

def formulario_vehiculo(request):    
    return render(request,"appdatos/formulariovehiculo.html")    

def formulario_vivienda(request):    
    return render(request,"appdatos/formulariovivienda.html")    

