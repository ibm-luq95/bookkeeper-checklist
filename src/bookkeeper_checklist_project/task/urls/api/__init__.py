# -*- coding: utf-8 -*-#
from django.urls import path, include
from task.views.api import (
    CreateTaskApiView,
    SetTaskCompletedApiView,
    RetrieveTaskApiView,
    TaskRetrieveAPIView,
    DeleteTaskApiView,
    UpdateTaskApiView,
)

app_name = "api"

urlpatterns = [
    path(
        "set-completed",
        SetTaskCompletedApiView.as_view(),
        name="set-task-completed",
    ),
    path(
        "retrieve-task",
        TaskRetrieveAPIView.as_view(),
        name="retrieve",
    ),
    path(
        "create",
        CreateTaskApiView.as_view(),
        name="create",
    ),
    path(
        "retrieve",
        RetrieveTaskApiView.as_view(),
        name="retrieve",
    ),
    path(
        "update",
        UpdateTaskApiView.as_view(),
        name="update",
    ),
    path(
        "delete",
        DeleteTaskApiView.as_view(),
        name="delete",
    ),
    path("templates/", include("task.urls.api.templates"), name="task-templates-api-urls"),
    # path(
    #     "bookkeeper/", include("task.urls.api.bookkeeper"), name="bookkeeper-task-api-urls"
    # ),
]
