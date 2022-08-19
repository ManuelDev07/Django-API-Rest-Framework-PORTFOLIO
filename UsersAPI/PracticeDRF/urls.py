from django.contrib import admin
from django.urls import path, include

#Swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Practice API",
      default_version='v1',
      description="This API is only for my practices :D",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="manudesarrolla07@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    #Users App:
    path('users/', include('UsersApp.urls')),

    #Swagger:
   path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
