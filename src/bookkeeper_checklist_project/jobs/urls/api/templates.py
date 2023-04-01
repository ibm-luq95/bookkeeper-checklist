# -*- coding: utf-8 -*-#
from django.urls import path, include

from jobs.views.api import JobRetrieveTemplateApi, CreateNewJobFromTemplateApi

app_name = "templates"

urlpatterns = [
    path("retrieve/<uuid:pk>", JobRetrieveTemplateApi.as_view(), name="retrieve"),
    path(
        "create_job_from_template/",
        CreateNewJobFromTemplateApi.as_view(),
        name="create-job-from-template",
    ),
]
