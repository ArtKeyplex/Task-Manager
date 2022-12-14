import json
import time
from datetime import date

from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import ToDoList, ToDoItem, TimeTracker
from .forms import ToDoItemPost, TimeTrackerForm


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
            task.user = request.user
            task.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, template, context)


def view_tasks(request):
    tasks = ToDoItem.objects.all().filter(user=request.user)
    page_obj = make_paginator(request, tasks, 5)
    today_day = date.today()
    template = 'todo_app/view_task.html'
    context = {
        'page_obj': page_obj,
        'today_day': today_day
    }
    return render(request, template, context)


def time_tracker(request):
    template = 'todo_app/view_trackers.html'
    user = request.user
    track = TimeTracker.objects.all().filter(user=user)
    page_obj = make_paginator(request, track, 4)
    context = {
        'page_obj': page_obj,
        'track': track,
    }
    return render(request, template, context)


def add_tracker(request):
    template = 'todo_app/add_tracker.html'
    form = TimeTrackerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            track = form.save(commit=False)
            track.user = request.user
            track.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, template, context)


def tracker_profile(request, slug):
    template = 'todo_app/one_tracker.html'
    track = get_object_or_404(TimeTracker, slug=slug)
    form = TimeTrackerForm(
        request.POST or None,
        files=request.FILES or None,
        instance=track
    )

    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        sec = int(post_data['sec'])
        min = int(post_data['min']) * 60
        TimeTracker.objects.filter(slug=slug).update(final_time=F('final_time') + sec + min)
    ty_res = time.gmtime(track.final_time)
    res = time.strftime("%d:%H:%M:%S", ty_res)
    context = {
        'track': track,
        'form': form,
        'res': res
    }
    return render(request, template, context)

