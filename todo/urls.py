from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # This is the path for the main todo list view
    path('add/', views.add_todo, name='add_todo'),  # Path for adding a new todo item
]
