from django.urls import path
from . import views



urlpatterns = [
    path('', views.ListListView.as_view(), name="index"),
    path('add/', views.add_task, name='add'),
    path('view/', views.view_tasks, name='view'),
]
