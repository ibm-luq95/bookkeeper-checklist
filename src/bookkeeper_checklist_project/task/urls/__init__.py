# -*- coding: utf-8 -*-#
from django.urls import path, include
from task.views import (
    TaskDeleteView,
    TaskCreateView,
    TasksArchiveListView,
    TasksListView,
    TaskUpdateView,
)

app_name = "task"

urlpatterns = [
    path("api/", include("task.urls.api"), name="task-api-urls"),
    # path("manager/", include("task.urls.manager"), name="task-manager-urls"),
    path("", TasksListView.as_view(), name="list"),
    path("create", TaskCreateView.as_view(), name="create"),
    path("delete/<uuid:pk>", TaskDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", TaskUpdateView.as_view(), name="update"),
    path("archive", TasksArchiveListView.as_view(), name="archive"),
]
