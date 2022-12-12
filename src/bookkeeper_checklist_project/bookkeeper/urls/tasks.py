# -*- coding: utf-8 -*-#
from django.urls import path
from bookkeeper.views import TaskListView, TaskUpdateView

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="list"),
    path("<uuid:pk>", TaskUpdateView.as_view(), name="details"),
]
