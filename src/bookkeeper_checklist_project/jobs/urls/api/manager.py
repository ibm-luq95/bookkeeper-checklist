# -*- coding: utf-8 -*-#
from django.urls import path

from jobs.views.api import (
    CreateJobManagerApiView,
    RetrieveJobManagerApiView,
    UpdateJobManagerApiView,
    DeleteJobManagerApiView,
)

app_name = "manager"

urlpatterns = [
    path(
        "create",
        CreateJobManagerApiView.as_view(),
        name="create",
    ),
    path("retrieve", RetrieveJobManagerApiView.as_view(), name="retrieve"),
    path("update", UpdateJobManagerApiView.as_view(), name="update"),
    path("delete", DeleteJobManagerApiView.as_view(), name="delete"),
]
