from django.contrib import admin
from .models import *


# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    ordering= ('id', 'nombre', 'activado', 'fecha_creacion')
    search_files=('id', 'nombre', 'activado', 'fecha_creacion')
    list_display= ('id', 'nombre', 'activado', 'fecha_creacion')
    list_filter=('activado',)

admin.site.register(Categoria, CategoriaAdmin)
