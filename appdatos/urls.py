from django.contrib import admin
from django.urls import path
from views import *

urlpatterns = [
    path("inicio",inicio,name="inicio"),

    path("individuo/",individuo,name="individuo"),
    path("vehiculo/",vehiculo,name="vehiculo"),
    path("vivienda/",vivienda,name="vivienda"),
    


    path("formulario_individuo/",formulario_individuo,name="formularioindividuo"),
    path("formulario_vehiculo/",formulario_vehiculo,name="formulariovehiculo"),
    path("formulario_vivienda/",formulario_vivienda,name="formulariovivienda"),
    path("formulario_individo/",formulario_individuo,name="formularioindividuo"),

]