from django.urls import path
from . import views

urlpatterns = [
    path('tiempo/', views.tiempo_view, name='tiempo'),
]