#Django
from django.urls import path

#views
from AuthUsersApp import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutApiView.as_view())
]
