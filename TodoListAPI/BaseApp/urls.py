# django libraries
from django.urls import path

# views BaseApp
from BaseApp import views

urlpatterns = [
    path('tasks/', views.todo_apiview),
    path('tasks/<int:task_id>/', views.todo_apiview_detail)
]