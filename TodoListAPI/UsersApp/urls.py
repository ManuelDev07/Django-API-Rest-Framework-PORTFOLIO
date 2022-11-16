# django libraries
from django.urls import path

# views UsersApp
from UsersApp import views

urlpatterns = [
    path('register/', views.UserRegistration.as_view()),
]