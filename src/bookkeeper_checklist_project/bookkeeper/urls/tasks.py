# -*- coding: utf-8 -*-#
from django.urls import path
from bookkeeper.views import TaskListView, TaskDetailView

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="list"),
    path("<uuid:pk>", TaskDetailView.as_view(), name="details"),
]
