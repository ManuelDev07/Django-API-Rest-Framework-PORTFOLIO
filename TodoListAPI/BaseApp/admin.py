# django libraries
from django.contrib import admin

# models BaseApp
from .models import TodoListModel

# Model's Visualitation in Admin Panel
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'title', 'completed', 'created_at']
    search_fields = ['task_id', 'title']
    list_filter = ['completed', 'created_at']
    readonly_fields = ['created_at']

# Register your models here.
admin.site.register(TodoListModel, TodoListAdmin)