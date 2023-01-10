# -*- coding: utf-8 -*-#
from django.urls import path
from manager.views import (
    TasksListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TasksArchiveListView,
)

app_name = "task"

urlpatterns = [
    path("", TasksListView.as_view(), name="list"),
    path("archive", TasksArchiveListView.as_view(), name="archive"),
    path("create", TaskCreateView.as_view(), name="create"),
    # path("details/<uuid:pk>", JobDetailsView.as_view(), name="details"),
    path("update/<uuid:pk>", TaskUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", TaskDeleteView.as_view(), name="delete"),
]
