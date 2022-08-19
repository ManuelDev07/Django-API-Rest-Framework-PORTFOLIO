from django.urls import include
from rest_framework.routers import DefaultRouter
from mainApp import views

#Creo el router:
router = DefaultRouter()

#Registrar:
router.register(r'car-brands', views.CarBrandsViewSet, basename='car-brands')
router.register(r'model-car', views.ModelCarsViewSet, basename='model-car')

urlpatterns = router.urls