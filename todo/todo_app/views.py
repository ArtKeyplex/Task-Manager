from datetime import date

from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import ToDoList, ToDoItem
from .forms import ToDoItemPost


class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"


def make_paginator(request, object, pages):
    paginator = Paginator(object, pages)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def add_task(request):
    template = 'todo_app/add_task.html'
    form = ToDoItemPost(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, template, context)


def view_tasks(request):
    tasks = ToDoItem.objects.all().filter()
    page_obj = make_paginator(request, tasks, 5)
    today_day = date.today()
    template = 'todo_app/view_task.html'
    context = {
        'page_obj': page_obj,
        'today_day': today_day
    }
    return render(request, template, context)
