from django import forms
from .models import ToDoItem


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = [
            "title",
            "description",
            "completed",
        ]  # Include the fields for the form
