"""TodoListAPI URL Configuration

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
# django libraries
from django.contrib import admin
from django.urls import path, include, re_path

# django rest framework libraries
from rest_framework import permissions

# SimpleJWT libraries
from rest_framework_simplejwt.views import TokenRefreshView

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# token_conf
from BaseApp.token_conf.views import MyTokenObtainPairView

# Swagger Doc Conf
schema_view = get_schema_view(
   openapi.Info(
      title="ToDo List API",
      default_version='v1',
      description="API de Práctica para el uso de TOKENS con SimpleJWT.",
      terms_of_service="https://www.manuapp.com/policies/terms/",
      contact=openapi.Contact(email="manueldesarrolla07@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    #SimpleJWT
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    

    # rest framework
    path('api-auth/', include('rest_framework.urls')),

    # APIViews BaseApp
    path('todo-list/', include('BaseApp.urls')),
]