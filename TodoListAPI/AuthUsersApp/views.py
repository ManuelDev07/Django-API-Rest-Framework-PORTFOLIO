#SimpleJWT
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

# serializer
from .serializers import MyUserSerializer

# token_config
from BaseApp.token_conf.serializers import MyTokenObtainPairSerializer

# Django
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Función SimpleJWT para dar el token a cada usuario manualmente
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # credenciales del usuario
        username = request.data.get('username')
        password = request.data.get('password')

        #autentico con los datos obtenidos
        user = authenticate(
            request, 
            username=username, 
            password=password
        )

        # verifico la data
        if user is not None:
            my_login_serializer = self.serializer_class(data=request.data)

            # y que los datos sean correctos
            if my_login_serializer.is_valid():
                user_serializer = MyUserSerializer(user)

                # le doy el token al usuario 
                token = get_tokens_for_user(user=user)

                return Response({'token':token, 'user':user_serializer.data}, status=status.HTTP_200_OK)
        else: # caso contrario devuelvo un código de error 
            return Response({'message':'Invalid Credentials.'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        #queryset
        user = User.objects.filter(pk=request.data.get('id'))

        # Si el usuario existe el token será bloqueado para cerrar su sesión
        if user:
            token = RefreshToken.for_user(user.first())
            token.blacklist()
            
            return Response({'message':'User Session Closed Successfully.'}, status=status.HTTP_200_OK)
        else: #caso contrario de no existir se devuelve un código de error 404
            return Response({'message':'User Not Found.'}, status=status.HTTP_404_NOT_FOUND)