from django.urls import path
from . import views
from django.urls import path, include
from rest_framework import routers
from .views import FriendViewSet

"""
urlpatterns = [ 
    path("directorio/", views.directorio, name="Directorio"),
]
"""
router = routers.DefaultRouter()
router.register(r'friends', FriendViewSet)

urlpatterns = [
    path('', include(router.urls))
]