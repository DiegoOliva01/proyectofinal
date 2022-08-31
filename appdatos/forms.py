from django import forms


class FormularioIndividuo(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    dni=forms.IntegerField()
    num_telefono=forms.IntegerField()
    estado_civil=forms.CharField(max_length=50)
    hijos=forms.IntegerField()
    trabajo=forms.CharField(max_length=50)
    def __str__(self):
        return self.nombre+""+self.apellido+""+str(self.dni)

class FormularioVehiculo(forms.Form):
    modelo=forms.CharField(max_length=50)  
    marca=forms.CharField(max_length=50)
    año_vehiculo=forms.IntegerField()
    patente=forms.CharField(max_length=50) 
    valor=forms.FloatField()
    dueño_vehiculo=forms.CharField(max_length=50)
    def __str__(self):
        return self.marca+""+self.modelo+""+str(self.patente)

class FormularioVivienda(forms.Form):
    direccion=forms.CharField(max_length=50)
    largo_terreno=forms.FloatField()
    ancho_terreno=forms.FloatField()
    largo_casa=forms.FloatField()
    ancho_casa=forms.FloatField()
    titular_terreno=forms.CharField(max_length=50)
    cant_personas_en_casa=forms.IntegerField()
    def __str__(self):
        return self.titular_terreno+""+self.direccion        