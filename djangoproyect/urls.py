"""
URL configuration for djangoproyect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from .views import inicio
from .views import portafolio
from .views import contacto
from .views import resumen
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.urls import path
from . import views
from rest_framework.documentation import include_docs_urls

from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name="inicio"),
    path('portafolio/', portafolio, name="portafolio"),
    path('contacto/', contacto, name="contacto"),
    path('resumen/', resumen, name="resumen"),
    path("", include('Aplicaciones.portafolio.urls')),  
    path("", include('Aplicaciones.contacto.urls')),  
    path("", include('Aplicaciones.ubicacion.urls')),  
    path("", include('Aplicaciones.tiempo.urls')),  
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path("accounts/", include('django.contrib.auth.urls')),
    path('exit/', views.exit, name="exit"),
    path("api/v1/", include('Aplicaciones.directorio.urls')),
    path("docs/", include_docs_urls(title='Api Documentation')), 
]

