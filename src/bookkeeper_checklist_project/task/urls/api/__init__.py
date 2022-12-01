# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("manager/", include("task.urls.api.manager"), name="manager-task-api-urls"),
    path(
        "bookkeeper/", include("task.urls.api.bookkeeper"), name="bookkeeper-task-api-urls"
    ),
]
