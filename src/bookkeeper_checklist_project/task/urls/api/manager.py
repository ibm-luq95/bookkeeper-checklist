# -*- coding: utf-8 -*-#
from django.urls import path

from task.views.api import (
    CreateTaskManagerApiView,
    RetrieveTaskManagerApiView,
    UpdateTaskManagerApiView,
    DeleteTaskManagerApiView,
)

app_name = "manager"

urlpatterns = [
    path(
        "create",
        CreateTaskManagerApiView.as_view(),
        name="create",
    ),
    path(
        "retrieve",
        RetrieveTaskManagerApiView.as_view(),
        name="retrieve",
    ),
    path(
        "update",
        UpdateTaskManagerApiView.as_view(),
        name="update",
    ),
    path(
        "delete",
        DeleteTaskManagerApiView.as_view(),
        name="delete",
    ),
]
