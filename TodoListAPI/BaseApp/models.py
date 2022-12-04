from django.db import models

# Create your models here.
# django libraries
from django.db import models

# rest framework
from rest_framework.serializers import ValidationError

# Validadores:
def validate_description(desc):
    if not desc:
        raise ValidationError('Debe tener una descripción la tarea.')
    elif len(desc) <= 2:
        raise ValidationError('La descripción de la tarea debe ser más larga.')

# Create your models here.
class TodoListModel(models.Model):
    '''Modelo de la Base de Datos para la App ToDo List'''
    
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Título de la Tarea')
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='Descripción de la Tarea', validators=[validate_description])
    completed = models.BooleanField(default=True, verbose_name='¿Completada?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el:')

    class Meta:
        db_table = 'lista_de_tareas'
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self) -> str:
        return self.title