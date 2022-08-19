from django.db import models
from django .contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email=email) #.lower()
        user = self.model( #data from the user
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        user.set_password(password) #set password
        user.save(using=self._db) #save data in DDBB

        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password, **extra_fields):
        user = self._create_user(username, email, name, last_name, password, False, False, **extra_fields) #Create a normal user

        #Superuser settings:
        user.is_superuser = True
        user.is_staff = True

        #Save the user in the DDBB
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=80, unique=True, blank=False, null=True, verbose_name='Nombre de Usuario')
    email = models.EmailField(max_length=100, unique=True, blank=False, null=True, verbose_name='Dirección de Correo Electrónico')
    name = models.CharField(max_length=150, verbose_name='Nombre(s)')
    last_name = models.CharField(max_length=150, verbose_name='Apellido(s)')
    is_active = models.BooleanField(default=True, verbose_name='¿Es Activo?')
    is_staff = models.BooleanField(default=False, verbose_name='¿Forma Parte del Staff?')

    objects = UserProfileManager() #Instancio la clase

    USERNAME_FIELD = 'username' #Login admin/
    REQUIRED_FIELDS = ['password', 'email', 'name', 'last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username