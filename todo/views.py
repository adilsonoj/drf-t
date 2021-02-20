from rest_framework import viewsets
from todo.models import Todo
from .serializer import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """Exibe todos as Tarefas"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer