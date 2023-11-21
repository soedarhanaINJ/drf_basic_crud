from django.shortcuts import render
from rest_framework import generics
from .serializers import ToDoSerializer
from todolist.models import ToDo

# CRUD Operations
class CreateTodoView(generics.CreateAPIView): # Create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ToDoListView(generics.ListAPIView): # Read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailToDoView(generics.UpdateAPIView): # Update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteToDoView(generics.DestroyAPIView): # Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
