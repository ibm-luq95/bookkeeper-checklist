# -*- coding: utf-8 -*-#
from django.urls import path, include
from jobs.views.api import (
    CreateJobApiView,
    RetrieveJobApiView,
    UpdateJobApiView,
    UpdateJobStatusApiView,
    DeleteJobApiView,
)

app_name = "api"

urlpatterns = [
    path(
        "create",
        CreateJobApiView.as_view(),
        name="create",
    ),
    path("retrieve", RetrieveJobApiView.as_view(), name="retrieve"),
    path("update", UpdateJobApiView.as_view(), name="update"),
    path("delete", DeleteJobApiView.as_view(), name="delete"),
    path("update-status", UpdateJobStatusApiView.as_view(), name="update-job-status"),
    path("templates/", include("jobs.urls.api.templates"), name="jobs-api-templates-urls"),
]
