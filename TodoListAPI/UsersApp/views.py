# django user Model
from django.contrib.auth.models import User

# rest framework
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny

# UsersApp Serializer
from .serializers import UserSerializer

# Create your views here.
class UserRegistration(generics.CreateAPIView):
    #queryset
    try:
        queryset = User.objects.all()
    except User.DoesNotExist:
        Response({'mensaje':'Información no Encontrada.'}, status=status.HTTP_404_NOT_FOUND)

    serializer_class = UserSerializer
    permission_classes = (AllowAny, )