from xml.etree.ElementInclude import include
from django.urls import path, include
from mainApp import views


urlpatterns = [
    path('countries/', views.countriesAPIView_get_post, name='get_post_countries'),
    
    #Countries:
    path('countries/<slug:slug>/', views.countriesAPIView_put_delete, name='put_delete_countries'),

    #ViewSets_:
    path('', include('mainApp.routers')),
]

