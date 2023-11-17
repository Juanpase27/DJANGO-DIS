from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.

def inicio(request):
    return render(request,"pages/inicio.html",{})

def portafolio(request):
    return render(request,"pages/portafolio.html",{})

def resumen(request):
    return render(request,"pages/resumen.html",{})

def contacto(request):
    return render(request,"pages/contacto.html",{})

@login_required
def resumen(request):
    return render(request,"pages/resumen.html",{})

def exit(request):
    logout(request)
    return redirect('inicio')