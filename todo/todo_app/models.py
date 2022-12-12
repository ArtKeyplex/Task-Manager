from django.db import models
from django.contrib.auth import get_user_model
from .helpers import slugify

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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-due_date"]

    def __str__(self):
        return self.title


class TimeTracker(models.Model):
    task = models.CharField(
        max_length=80, verbose_name='Название'
    )
    slug = models.SlugField()
    final_time = models.IntegerField(default=0)
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    counting = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.task)

        super(TimeTracker, self).save(*args, **kwargs)

    def __str__(self):
        return self.task
