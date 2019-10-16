from django.contrib import admin

from Apps.Usuario.models import Usuario,Administrador,Chef
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Chef)