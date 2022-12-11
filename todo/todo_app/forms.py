from django import forms

from .models import ToDoItem


class ToDoItemPost(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'due_date', 'todo_list',]
        widgets = {
            'description': forms.Textarea
        }