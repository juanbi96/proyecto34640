from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import loader, Template

# Create your views here.

def familiar(request):

    familiar1=Familiar(nombre="Juan", apellido="Biet", edad=26, fecha_nacimiento="1996-11-05")
    familiar1.save()

    familiar2=Familiar(nombre="Josefina", apellido="Biet", edad=16, fecha_nacimiento="2006-07-07")
    familiar2.save()

    familiar3=Familiar(nombre="Catalina", apellido="Biet", edad=23, fecha_nacimiento="1999-05-05")
    familiar3.save()

    diccionario={
        "Nombre1":familiar1.nombre+" "+familiar1.apellido,
        "Edad1": familiar1.edad,
        "Fecha_nacimiento1": familiar1.fecha_nacimiento,

        "Nombre2":familiar2.nombre+" "+familiar2.apellido,
        "Edad2": familiar2.edad,
        "Fecha_nacimiento2": familiar2.fecha_nacimiento,

        "Nombre3":familiar3.nombre+" "+familiar3.apellido,
        "Edad3": familiar3.edad,
        "Fecha_nacimiento3": familiar3.fecha_nacimiento
        }

    plantilla=loader.get_template("templates.html")

    documento=plantilla.render(diccionario)

    return HttpResponse(documento)
    

    #cadena_Texto="Familiares: "+familiar1.nombre+" "+familiar1.apellido+", "+familiar2.nombre+" "+familiar2.apellido+", "+familiar3.nombre+" "+familiar3.apellido