from dataclasses import fields
from .models import CarBrandsModel, CountriesModel, ModelCarModel
from rest_framework import serializers

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountriesModel
        fields = ('id','name','flag')

class CarBrandSerializer(serializers.ModelSerializer):

    #Relacion en cuanto a los países:
    country = CountriesSerializer()

    class Meta:
        model = CarBrandsModel
        fields = ('id', 'brand', 'image','country')

class ModelCarSerializer(serializers.ModelSerializer):

    #Relación con los países y marcas de autos:
    country = CountriesSerializer()
    brand = CarBrandSerializer()

    class Meta:
        model = ModelCarModel
        fields = ('id', 'car_model', 'description','brand', 'image','country')