from rest_framework import serializers
from profiles_api import models #para crear los perfiles de usuarios basandome en esos modelos mediante una clase

class UserProfileSerializer(serializers.ModelSerializer):#Serializar los datos de un usuario
    """Serializará los datos del perfil de un usuario"""

    class Meta:
        model = models.UserProfile #Heredo el modelo de UserProfile
        
        #Defino los campos de mi modelo para crear los usuarios
        #Estos serán los datos que se guardarán y se verán en la API 
        fields = ('id', 'email', 'name', 'password')
        
        #Configuro el campo de Password para que no se vea el texto al ingresarse en el input 
        # y se serializará la password para que al mostrarse la API se vea todo menos la contraseña del usuario(proteger/serializar)
        extra_kwargs = {
            'password':{
                'write_only':True, #solo escribir mas no ver en la API
                'style':{'input_type':'password'} #Para que salga protegida la contraseña (con puntos/asteriscos mientras se escribe)
            }
        }

    #Sobrescribo la función de create():
    #Para sobrescribir una función debo definir que función es la que tengo que sobrescribir
    def create(self, validated_data):
        '''Esta función creará y devolverá un nuevo usuario'''
        #se instancia la clase UserProfile y creo un nuevo usuario:
        user = models.UserProfile.objects.create_user( #el create_user es el nombre del método de ese modelo (al cual estaré sobrescribiendo)
            #creo los campos que quiero validar:
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Esta función actualizará los datos de un usuario en específico"""

        if 'password' in validated_data: #Si la contraseña existe y está validada
            password = validated_data.pop('password')
            instance.set_password(password)

            #Y de esta manera el usuario podrá hacer login para acceder a su cuenta

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):#Serializar el feed de un usuario
    """Serializará los datos del feed de los usuarios"""

    class Meta:
        model = models.ProfileFeedItem #Heredo el modelo para recibir la info
        
        #Campos:
        fields = ('id', 'user_profile', 'status_text','created_at')
        
        #Solo se serializarán el user_profile :
        extra_kwargs = {'user_profile':{'read_only':True}} #Para solo ver los datos

        def perform_create(self, serializer):
            """Este método se encargará de hacer un set (setear) del perfil de usuario para el usuario que está logeado"""
            
            serializer.save(user_profile=self.request.user)