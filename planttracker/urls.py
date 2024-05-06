"""planttracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from planttrackerapi.views import PlantView, LogView, register, login

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'plants', PlantView, 'plant')
router.register(r'logs', LogView, 'log')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register),
    path('login', login),
    path('admin/', admin.site.urls),
]
