from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings #para obtener los settings que se definieron en settings.py

# Create your models here.
class UserProfileManager(BaseUserManager): #Para crear usuarios y superusuarios
    """Clase para la configuración y creación de usuarios y SuperUsuarios"""

    def create_user(self, email, name, password=None):
        """Esta función creará un usuario común en la BBDD"""
        
        if not email:
            raise ValueError('ERROR! Es necesario registrar el EMAIL!')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Esta función creará un SuperUsuario en la BBDD"""

        user = self.create_user(email, name, password) #Llamada a la función para crear el usuario común

        #Lo configuro como superuser:
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):#para ingresar los datos de un usuario 
    """Este clase/modelo se encargará de obtener todos los datos de un usuario y crearlo en la BBDD"""

    #Se establecen que datos serán los que tendrá el usuario
    email = models.EmailField(max_length=150, unique=True, verbose_name='Correo Electrónico')
    name = models.CharField(max_length=200, verbose_name='Nombre')
    is_active = models.BooleanField(default=True, verbose_name='¿Es un Usuario Activo?')
    is_staff = models.BooleanField(default=False, verbose_name='¿Es un Staff?')

    #Creo y guardo el usuario instanciando la clase:
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

class ProfileFeedItem(models.Model): #El feed con todos los datos de un usuario
    """Perfil de un usuario"""
    #relación uno a uno:
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Perfil del Usuario') #La conf de settings.py
    status_text = models.CharField(max_length=255, verbose_name='Texto de Estado') #El contenido de la publicación
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    def _str__(self):
        return self.status_text