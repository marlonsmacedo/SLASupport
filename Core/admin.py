from django.contrib import admin
from .models import  Area, Problema, Categoria_Problema, Chamado, Status_Chamado

admin.site.register(Area)
admin.site.register(Problema)
admin.site.register(Categoria_Problema)
admin.site.register(Chamado)
admin.site.register(Status_Chamado)