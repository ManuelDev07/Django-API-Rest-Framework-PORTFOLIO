from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

#Creo mi router:
router = DefaultRouter()
#Registro la URL:
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [    
    #Registro los viewset:
    path('', include(router.urls)),

    #El área de Login:
    path('login/', views.UserLoginApiView.as_view())
]