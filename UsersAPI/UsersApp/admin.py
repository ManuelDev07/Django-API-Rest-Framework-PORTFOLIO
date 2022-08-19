from django.contrib import admin
from .models import UserProfile

#Visualization Models in Panel Admin:
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name','last_name','username', 'email', 'is_active', 'is_superuser']
    search_fields = ['name', 'last_name', 'username', 'email']
    list_filter = ['name','last_name','username', 'email', 'is_active', 'is_superuser']

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)

#Django Admin Panel conf/personalization:
admin.site.site_header = 'Administración de Usuarios'
admin.site.index_title = 'Configuración de Datos de Usuarios'