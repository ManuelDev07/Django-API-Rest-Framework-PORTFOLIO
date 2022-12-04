# django rest framework libraries
from rest_framework import serializers

# models BaseApp
from .models import TodoListModel

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListModel
        fields = '__all__'