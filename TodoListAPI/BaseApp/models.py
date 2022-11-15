# django libraries
from django.db import models

# Create your models here.
class TodoListModel(models.Model):
    '''Modelo de la Base de Datos para la App ToDo List'''
    
    task_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name='Título de la Tarea')
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='Descripción de la Tarea')
    completed = models.BooleanField(default=True, verbose_name='¿Completada?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el:')

    class Meta:
        db_table = 'Lista de Tareas'
        verbose_name = 'Lista de Tarea'
        verbose_name_plural = 'Lista de Tareas'

    def __str__(self) -> str:
        return self.title