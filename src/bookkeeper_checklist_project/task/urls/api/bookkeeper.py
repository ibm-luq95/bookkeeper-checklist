# -*- coding: utf-8 -*-#
from django.urls import path

from task.views.api import SetTaskCompletedBookkeeperApiView, TaskBookkeeperRetrieveAPIView

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
]
