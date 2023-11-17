from django.shortcuts import render
from . models import Contacto

# Create your views here.
def contactos(request):
    if request.method == "POST":
        tname = request.POST["name"]
        temail = request.POST["email"]
        tphone = request.POST["phone"]
        tmessage = request.POST["message"]
        obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
        obj_contact.save()
        #return HttpResponse("EL registro fue ingresado")
        #email(obj_contact)
        return render(request,"pages/gracias.html",)
    else:
        return render(request,"pages/gracias.html",)
    #mis_proyectos = Proyecto.objects.all()
    #return render(request,"pages/contacto.html",)