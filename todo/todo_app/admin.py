from django.contrib import admin
from todo_app.models import ToDoItem, ToDoList, TimeTracker

admin.site.register(ToDoItem)
admin.site.register(ToDoList)
admin.site.register(TimeTracker)