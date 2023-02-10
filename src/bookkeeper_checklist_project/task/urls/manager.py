# -*- coding: utf-8 -*-#
from django.urls import path

from task.views import (
    ManagerTaskUpdateView,
    ManagerTasksArchiveListView,
    ManagerTaskDeleteView,
    ManagerTaskCreateView,
    ManagerTasksListView,
)

app_name = "manager"

urlpatterns = [
    path("", ManagerTasksListView.as_view(), name="list"),
    path("create", ManagerTaskCreateView.as_view(), name="create"),
    path("delete/<uuid:pk>", ManagerTaskDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", ManagerTaskUpdateView.as_view(), name="update"),
    path("archive", ManagerTasksArchiveListView.as_view(), name="archive"),
]
