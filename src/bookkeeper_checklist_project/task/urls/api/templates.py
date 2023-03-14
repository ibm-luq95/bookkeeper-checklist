# -*- coding: utf-8 -*-#
from django.urls import path, include

from task.views.api import (
    TaskTemplateRetrieveAPIView,
    CreateTaskItemApiView,
    TaskTemplateDeleteAPIView,
    CreateTaskTemplateApiView,
)

app_name = "templates"

urlpatterns = [
    path("retrieve/<uuid:pk>", TaskTemplateRetrieveAPIView.as_view(), name="retrieve"),
    path("delete/<uuid:pk>", TaskTemplateDeleteAPIView.as_view(), name="delete"),
    path("create_item", CreateTaskItemApiView.as_view(), name="create-task-item"),
    path(
        "create_task_template",
        CreateTaskTemplateApiView.as_view(),
        name="create-task-template",
    ),
]
