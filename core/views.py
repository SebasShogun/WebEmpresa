from django.shortcuts import render, HttpResponse

# Create your views here.
"""
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/
"""

def home(requeste):
    return HttpResponse("Inicio")

def about(requeste):
    return HttpResponse("Historia")

def services(requeste):
    return HttpResponse("Servicios")

def store(requeste):
    return HttpResponse("Visítanos")

def contact(requeste):
    return HttpResponse("Contacto")

def blog(requeste):
    return HttpResponse("Blog")

def sample(requeste):
    return HttpResponse("Sample")

