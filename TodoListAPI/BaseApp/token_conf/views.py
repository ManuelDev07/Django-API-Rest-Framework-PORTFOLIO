# SimpleJWT
from rest_framework_simplejwt.views import TokenObtainPairView

# serializers token_conf
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer