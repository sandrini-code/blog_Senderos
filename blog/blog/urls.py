"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from apps.post.views import  crearPost, plantillaHija1, plantillaHija2, blog, quienesSomos, formularioContacto, contactar
#from MiProyecto.view import plantillaHija1, plantillaHija2, blog, quienesSomos, formularioContacto, contactar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_post/', crearPost, name='crear_post'),
    path("plantillaHija1/", plantillaHija1),
    path("plantillaHija2/", plantillaHija2),
    path("", blog),
    path("quienesSomos/", quienesSomos),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar),

]
