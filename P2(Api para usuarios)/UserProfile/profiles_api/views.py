from rest_framework import viewsets, filters
from rest_framework.response import Response 
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken #(Se trabaja como APIView)
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from profiles_api import serializers, models, permissions #*
#Response: para devolver objetos response a doc JSON
#status: es para devolver una respuesta del estado de la request
#filters: Para poder filtrar usuarios a través de mi API:
#*: importo los archivos serializers, models, permissions
#TokenAuthentication: Se usará para que los usuarios puedan autenticar sus datos en mi API, va de la mano con los permissions.py. Funciona generando un token_string aleatorio que se genera cuando se crea un usuario o se hace login y cada vez que se hace un request se tiene que verificar ese token
#ObtainAuthToken: se usará para poder realizar el área de login para los usuarios. Cada vez que un usuario haga login se le asignará un token aleatorio y así podrá hacer varias funciones dentro de su perfil
#IsAuthenticated: para que solo los usuarios autenticados tengan acceso al API

# Create your views here.
#Se usará ModelViewSet para manipular a los usuarios de los modelos a través de mi API
class UserProfileViewSet(viewsets.ModelViewSet): 
    """Creará y actualizará los perfiles de usuarios"""

    #Primero se serializa la informacion:
    serializer_class = serializers.UserProfileSerializer

    #Hago un QuerySet:
    queryset = models.UserProfile.objects.all() #Así obtengo todos los users creados

    #Configuro la autenticación correcta con los token y permisos:
    authentication_classes = (TokenAuthentication,) #el usuario se autentica
    permission_classes = (permissions.UpdateOwnProfile,) #el usuario se otorgan los permisos
    filter_backends = (filters.SearchFilter,) #filtros para búsquedas de usuarios
    search_fields = ('name', 'email',) #casilla de búsqueda para buscar por nombre y el correo 

class UserLoginApiView(ObtainAuthToken):
    """Esta clase se encargará de crear los token de autenticación para 
    c/usuario. Esto creará además los campos para hacer login"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Esta clase configurará la creación, lectura y actualizar el feed de un usuario"""

    serializer_class = serializers.ProfileFeedItemSerializer #Serializo la info
    authentication_classes = (TokenAuthentication,) #Se autentica el user
    #queryset:
    queryset = models.ProfileFeedItem.objects.all() #Se obtienen todos los items que hay en el modelo
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)#Se le otorgan los permisos si el usuario está autenticado