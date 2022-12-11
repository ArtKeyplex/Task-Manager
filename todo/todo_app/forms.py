from django import forms

from .models import ToDoItem, TimeTracker


class ToDoItemPost(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'due_date', 'todo_list',]
        widgets = {
            'description': forms.Textarea
        }


class TimeTrackerForm(forms.ModelForm):

    class Meta:
        model = TimeTracker
        fields = ['task', 'description']
        widgets = {
            'description': forms.Textarea
        }
