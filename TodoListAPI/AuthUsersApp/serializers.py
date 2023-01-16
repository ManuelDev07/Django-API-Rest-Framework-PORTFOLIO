# rest_framework
from rest_framework import serializers

#Django
from django.contrib.auth.models import User

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')