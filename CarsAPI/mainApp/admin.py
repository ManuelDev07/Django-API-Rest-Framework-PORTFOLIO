from django.contrib import admin
from .models import CarBrandsModel, CountriesModel, ModelCarModel

#Visualización de los modelos en Admin Panel:
class CarBrandsAdmin(admin.ModelAdmin):
    list_display = ['brand', 'country', 'state']
    search_fields = ['brand', 'country']
    list_filter = ['brand', 'country', 'state']

class CountriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    search_fields = ['name']
    list_filter = ['name', 'state']

class ModelCarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'brand', 'country','state']
    search_fields = ['car_model', 'brand', 'country']
    list_filter = ['car_model', 'brand', 'country']


# Register your models here.
admin.site.register(CarBrandsModel, CarBrandsAdmin)
admin.site.register(CountriesModel, CountriesAdmin)
admin.site.register(ModelCarModel, ModelCarAdmin)
