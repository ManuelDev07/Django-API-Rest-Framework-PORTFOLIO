#El include y DefaultRouter es para registrar el ViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

#Defino el router instanciando un objeto de la clase importada DefaultRouter:
router = DefaultRouter()
#Y registro la URL con el router. Sintaxis: router.register('nombreURL', views.nombreViewSet, base_name='nombre para identificar la URL')
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    #Registro la URL de mi APIView:
    #Al ser una clase se debe pasar como función, para ello uso el .as_view()
    path('hello-apiview/', views.HelloApiView.as_view()),

    #Los URL de los ViewSet se registran de una manera distinta: REQUIEREN EL USO DE LOS ROUTER
    #Luego registro el urlpatterns:
    path('', include(router.urls))
]