# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "task"

urlpatterns = [
    path("api/", include("task.urls.api"), name="task-api-urls"),
    path("manager/", include("task.urls.manager"), name="task-manager-urls"),
]
