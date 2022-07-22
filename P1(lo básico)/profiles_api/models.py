from django.db import models
#Import AbstractBaseUser, PermissionMixin y BaseUserManager sirve para crear la clase básica de creación de usuarios
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
#Se hereda el modelo importado BaseUserManager
#Creo el manager del usuario:
class UserProfileManager(BaseUserManager):
    '''Manager para manipular los perfiles de usuarios'''
    
    #Esto es para crear un usuario común:
    def create_user(self, email, name, password=None):
        '''Se crea un nuevo perfil de usuario'''
        #En caso de que no coloquen un email al registrar un usuario
        if not email:
            raise ValueError('ERROR! El usuario debe tener un email.')
        
        email = self.normalize_email(email) #para que todo se coloque minúscula
        user = self.model(email=email, name=name)

        #Creo el modelo de usuario:
        user.set_password(password)
        user.save(using=self._db)

        return user 
    
    #Una función para los administradores (superuser) para establecer que un user sea o no super usuario
    def create_superuser(self, email, name, password):
        #Creo el usuario llamando la función con los parámetros/datos:
        user = self.create_user(email, name, password)
        
        #lo configuro como superuser:
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


#Se hereda  AbstractBaseUser y PermissionMixin
#Establezco como quiero crear el usuario o superusuario al hacerse en consola y/o en una página con una view y template de Registro:
class UserProfile(AbstractBaseUser,  PermissionsMixin): #El PermissionsMixin es para combinar ambos datos de ambas tablas y poder llamar una a la otra
    """Modelo BBDD para crear usuarios al hacerse con el createsuperuser en consola PERO solo será para obtener los datos ya que la clase UserProfileManager
    será la que creará en si el usuario y lo guardará en la BBDD ya sea como usuario común o super usuario."""
    #Cada verbose_name= será como se mostará en consola
    email = models.EmailField(max_length=255, unique=True, verbose_name='Correo  Electrónico')
    name = models.CharField(max_length=255, verbose_name='Nombre')
    is_active = models.BooleanField(default=True, verbose_name='¿Usuario Activo?')
    is_staff = models.BooleanField(default=False, verbose_name='¿Es Staff?')

    #Se establece el custom user manager para el modelo de usuarios(es requerido por el django rest framework)
    objects = UserProfileManager() #Instancio la clase para así crear y guardar el usuario ya sea como común o superusuario.
    
    #Se define el campo del login que el usuario llenará -> NOTA: cuando acceda a la página de admin, tendré inciar sesión pero con el correo
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Ayudará a obtener el nombre completo del usuario'''
        return self.name
    
    def get_short_name(self):
        '''Ayudará a ver un nombre corto del usuario'''
        return self.name

    def __str__(self):
        '''Se devolverá una cadena que demuestre los datos del usuario'''
        return self.email