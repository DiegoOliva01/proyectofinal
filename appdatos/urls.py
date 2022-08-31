from django.contrib import admin
from django.urls import path
from appdatos import views

urlpatterns = [
    path("inicio/",views.inicio,name="inicio"),

    path("individuo/",views.individuo,name="individuo"),
    path("vehiculo/",views.vehiculo,name="vehiculo"),
    path("vivienda/",views.vivienda,name="vivienda"),
    


    path("formulario_individuo/",views.formulario_individuo,name="formularioindividuo"),
    path("formulario_vehiculo/",views.formulario_vehiculo,name="formulariovehiculo"),
    path("formulario_vivienda/",views.formulario_vivienda,name="formulariovivienda"),
    

]