# todo/forms.py
from django import forms
from .models import ToDoItem

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description']  # Ensure these fields exist in the model

