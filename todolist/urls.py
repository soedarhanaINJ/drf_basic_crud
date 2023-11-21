from django.urls import path
from todolist.views import CreateTodoView, ToDoListView, DetailToDoView, DeleteToDoView

urlpatterns = [
    path('', ToDoListView.as_view(), name='view_api'),
    path('create', CreateTodoView.as_view(), name='create_api'),
    path('<int:pk>', DetailToDoView.as_view(), name='update_api'),
    path('delete/<int:pk>', DeleteToDoView.as_view(), name='delete_api'),
]