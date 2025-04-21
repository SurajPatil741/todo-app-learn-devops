# todo/views.py
from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoForm  # assuming you have a form for creating ToDo items

def todo_list(request):
    todos = ToDoItem.objects.all()  # Get all to-do items from the database
    return render(request, 'todo/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new to-do item to the database
            return redirect('todo_list')  # Redirect to the list of to-dos
    else:
        form = ToDoForm()  # Display an empty form if it's a GET request

    return render(request, 'todo/add_todo.html', {'form': form})

