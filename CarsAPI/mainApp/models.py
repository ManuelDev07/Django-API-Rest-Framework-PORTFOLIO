from django.db import models

# Create your models here.
class CountriesModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='País')
    flag = models.CharField(max_length=255, verbose_name='URL de la Imágen')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    state = models.BooleanField(default=True, verbose_name='¿Mostrar?')

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self) -> str:
        return self.name

class CarBrandsModel(models.Model):
    brand = models.CharField(max_length=80, unique=True, blank=False, null=False, verbose_name='Nombre de la Marca')
    image = models.CharField(max_length=255, verbose_name='URL de la Imágen')
    country = models.ForeignKey(CountriesModel, on_delete=models.CASCADE, null=False, blank=False, verbose_name='País de Origen')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    state = models.BooleanField(default=True, verbose_name='¿Mostrar?')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self) -> str:
        return self.brand

class ModelCarModel(models.Model):
    car_model = models.CharField(max_length=255, unique=True, verbose_name='Modelo del Auto')
    description = models.CharField(max_length=500, verbose_name='Breve Descripción del Auto')
    image = models.CharField(max_length=255, verbose_name='URL de la Imágen')
    brand = models.ForeignKey(CarBrandsModel, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Marca Perteneciente')
    country = models.ForeignKey(CountriesModel, on_delete=models.CASCADE, blank=False, null=False, verbose_name='País de Origen')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    state = models.BooleanField(default=True, verbose_name='¿Mostrar?')

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self) -> str:
        return self.car_model