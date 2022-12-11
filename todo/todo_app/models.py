from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ToDoList(models.Model):
    title = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(
        max_length=80, verbose_name='Название'
    )
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание'
    )
    due_date = models.DateTimeField(
        verbose_name='Выберите дату события'
    )
    todo_list = models.ForeignKey(
        ToDoList, on_delete=models.CASCADE,
        null=True, blank=True, verbose_name='Выберите список дел'
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        ordering = ["-due_date"]

    def __str__(self):
        return self.title
