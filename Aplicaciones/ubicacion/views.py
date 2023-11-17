from django.shortcuts import render
from .models import Lugares
import folium
from folium.plugins import FastMarkerCluster

# Create your views here.
def sitios_interes(request):
    #Get my locations
    locations = Lugares.objects.all()
    #Define the initial map
    initialMap = folium.Map(location=[4.6539857,-74.1252444], zoom_start=11)
    #Creating the markets
    latitudes = [location.lat for location in locations]
    longitudes = [location.lng for location in locations]
    popups = [location.name for location in locations]
    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initialMap)
    
    #context = {'map':initialMap._repr_html_()}
    context = {'map':initialMap._repr_html_(), 'locations':locations}
    
    return render(request, 'mapa.html',context )
"""
def tiempo(request):
    city = input("Enter your city:  ")
    url = "api url".format(city) #https://openweathermap.org
    res = request.get(url)
    data = res.json()
    temp = data["main"]["temp"]
    vel_viento = data["wind"]["speed"]

    latitud = data["coord"]["lat"]
    longitud = data["coord"]["lon"]

    descripcion = data["weather"][0]["description"]

    print("Tempreratura: ", temp)
    print("Velocidad del viento: {} m/s".format(vel_viento))
    print("Latitud: {}".format(latitud))
    print("Longitud: {}".format(longitud))
    print("Descripción: {}".format(descripcion))"""