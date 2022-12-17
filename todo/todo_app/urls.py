from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListListView.as_view(), name="index"),
    path('add/', views.add_task, name='add'),
    path('view/', views.view_tasks, name='view'),
    path('time_tracker/all/', views.time_tracker, name='time_tracker'),
    path('time_tracker/new/', views.add_tracker, name='add_tracker'),
    path('time_tracker/<slug:slug>/', views.tracker_profile, name='tracker_profile'),
]
