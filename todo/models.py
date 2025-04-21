# todo/models.py
from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=200)  # Ensure this field exists
    description = models.TextField(default='No description')

    def __str__(self):
        return self.title

