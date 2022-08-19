from rest_framework import serializers
from .models import UserProfile, UserProfileManager

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializador para el Modelo de UserProfile que se encargará de recibir los datos de un usuario para luego guardarlos en la API y BBDD"""
    
    class Meta:
        model = UserProfile
        fields = ('id','name','username','email','password')

        def create(self, validated_data):
            user = UserProfile(**validated_data)
            user = UserProfile.objects.create_user(
                username = validated_data['username'],
                email = validated_data['email'],
                name = validated_data['name'],
                last_name = validated_data['last_name'],
                password = user.set_password(validated_data['password'])
            )

            user.save()
            
            return user
    
        def update(self, instance, validated_data):
            data_user_updated = super().update(instance, validated_data)
            data_user_updated.set_password(validated_data['password'])
            data_user_updated.save()

            return data_user_updated