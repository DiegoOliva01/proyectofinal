from django.shortcuts import render
from appdatos import *
from appdatos.models import Persona,Vehiculo,Vivienda
from appdatos.forms import FormularioIndividuo,FormularioVehiculo,FormularioVivienda
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

    if request.method=="POST":
        miformulario=FormularioIndividuo(request.POST)
        if miformulario.is_valid():
           info=miformulario.cleaned_data
           nombre=info.get("nombre") 
           apellido=info.get("apellido") 
           dni=info.get("dni") 
           edad=info.get("edad") 
           trabajo=info.get("trabajo") 
           hijos=info.get("hijos") 
           estado_civil=info.get("estado_civil") 
           num_telefono=info.get("num_telefono") 

           persona=Persona(nombre=nombre,apellido=apellido,edad=edad,dni=dni,trabajo=trabajo,hijos=hijos,estado_civil=estado_civil,num_telefono=num_telefono)
           persona.save()
           return render(request,"appdatos/inicio.html", {"mensaje": "Individuo creado"})
        else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error,no se pudo crear al individuo"} )    
    else:
        miformulario=FormularioIndividuo()
        return render(request,"appdatos/formularioindividuo.html", {"formulario":miformulario} )  

def formulario_vehiculo(request):    
    if request.method=="POST":
        miformulario=FormularioVehiculo(request.POST)
        if miformulario.is_valid():
           info=miformulario.cleaned_data
           marca=info.get("marca") 
           año_vehiculo=info.get("año_vehiculo") 
           patente=info.get("patente") 
           valor=info.get("valor") 
           dueño_vehiculo=info.get("dueño_vehiculo") 
          
       
           vehiculo=Vehiculo(marca=marca,año_vehiculo=año_vehiculo,patente=patente,valor=valor,dueño_vehiculo=dueño_vehiculo)
           vehiculo.save()
           return render(request,"appdatos/inicio.html", {"mensaje": "vehiculo registrado"})
        else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error,no se pudo registrar el vehiculo"} )    
    else:
        miformulario=FormularioVehiculo()
        return render(request,"appdatos/formulariovehiculo.html", {"formulario":miformulario} )    

def formulario_vivienda(request):  
    if request.method=="POST":
        miformulario=FormularioVivienda(request.POST)
        if miformulario.is_valid():
           info=miformulario.cleaned_data
           direccion=info.get("direccion")
           largo_terreno=info.get("largo_terreno") 
           ancho_terreno=info.get("ancho_terreno") 
           largo_casa=info.get("largo_casa") 
           ancho_casa=info.get("ancho_casa") 
           titular_terreno=info.get("titular_terreno")
           cant_personas_en_casa=info.get("cant_personas_en_casa")
 
           casa=Vivienda(largo_terreno=largo_terreno,largo_casa=largo_casa,ancho_casa=ancho_casa,ancho_terreno=ancho_terreno,titular_terreno=titular_terreno,cant_personas_en_casa=cant_personas_en_casa,direccion=direccion)
           casa.save()
           return render(request,"appdatos/inicio.html", {"mensaje": "Vivienda registrado"})
        else:   
           return render(request,"appdatos/inicio.html", {"mensaje": "Error,no se pudo registrar la vivienda"} )    
    else:
        miformulario=FormularioVivienda()
        return render(request,"appdatos/formulariovivienda.html", {"formulario":miformulario} )  
       








""" <form action="{% url 'inicio' %}" method="POST"> {% csrf_token %}
   
    <p>Nombre: <input type="text",name="nombre"></p>
    <p>Apellido: <input type="text",name="apellido"></p>
    <p>DNI: <input type="number",name="dni"></p>
    <p>Edad: <input type="number",name="edad"></p>
    <p>Trabajo: <input type="text",name="trabajo"></p>
    <p>Hijos: <input type="number",name="hijos"></p>
    <p>Estado civil: <input type="text",name="estado_civil"></p>
    <p>Numero de telefono: <input type="number",name="num_telefono"></p>

    <input type="submit" value="Enviar">



 </form>
 <h2>{{ mensaje }}</h2>"""