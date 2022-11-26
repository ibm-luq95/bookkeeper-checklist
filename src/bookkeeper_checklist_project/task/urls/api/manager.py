# -*- coding: utf-8 -*-#
from django.urls import path

from task.views.api import CreateTaskManagerApiView

app_name = "manager"

urlpatterns = [
    path(
        "create",
        CreateTaskManagerApiView.as_view(),
        name="create-task-manager",
    ),
]
