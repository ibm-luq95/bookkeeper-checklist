# -*- coding: utf-8 -*-#
from django.urls import path

from task.views.api import (
    SetTaskCompletedBookkeeperApiView,
    TaskBookkeeperRetrieveAPIView,
    CreateTaskBookkeeperApiView,
    UpdateTaskBookkeeperApiView,
    DeleteTaskBookkeeperApiView,
)

app_name = "bookkeeper"

urlpatterns = [
    path(
        "set-completed",
        SetTaskCompletedBookkeeperApiView.as_view(),
        name="set-task-completed",
    ),
    path(
        "retrieve-task",
        TaskBookkeeperRetrieveAPIView.as_view(),
        name="retrieve",
    ),
    # path(
    #     "retrieve-task/<uuid:pk>",
    #     TaskBookkeeperRetrieveAPIView.as_view(),
    #     name="retrieve",
    # ),
    path(
        "create",
        CreateTaskBookkeeperApiView.as_view(),
        name="create",
    ),
    path(
        "update",
        UpdateTaskBookkeeperApiView.as_view(),
        name="update",
    ),
    path(
        "delete",
        DeleteTaskBookkeeperApiView.as_view(),
        name="delete",
    ),
    path(
        "delete/<uuid:pk>",
        DeleteTaskBookkeeperApiView.as_view(),
        name="delete",
    ),
]
