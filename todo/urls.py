
from django.urls import path
from todo.views import get_todos, create_todo, delete_todo

urlpatterns = [
    path('todos/', get_todos, name='get_todos'),
    path('create-todo/', create_todo, name='create-todo'),
    path('delete-todo/<int:id>/', delete_todo, name='delete-todo'),
]
