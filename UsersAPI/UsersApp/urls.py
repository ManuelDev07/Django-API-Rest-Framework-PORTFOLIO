from django.urls import path, include
from UsersApp import views

urlpatterns = [
    path('', views.user_profile_get_postAPIView, name='all_users'),
    path('<int:id>', views.user_profile_get_put_deleteAPIView, name='user')
]