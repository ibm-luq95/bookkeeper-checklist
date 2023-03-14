# -*- coding: utf-8 -*-#
from django.urls import path, include

from documents.views.api import CreateDocumentTemplateApiView

app_name = "templates"

urlpatterns = [
    # path("retrieve/<uuid:pk>", TaskTemplateRetrieveAPIView.as_view(), name="retrieve"),
    # path("delete/<uuid:pk>", TaskTemplateDeleteAPIView.as_view(), name="delete"),
    path("create", CreateDocumentTemplateApiView.as_view(), name="create"),
    # path(
    #     "create_task_template",
    #     CreateTaskTemplateApiView.as_view(),
    #     name="create-task-template",
    # ),
]
