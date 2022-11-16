# django User Model
from django.contrib.auth.models import User

# django rest framework libraries
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'username', 'email', 'password'] # campos para el formulario de registro
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        return {"username":user.username, "email":user.email}