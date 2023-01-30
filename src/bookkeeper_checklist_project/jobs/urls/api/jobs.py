# -*- coding: utf-8 -*-#
from django.urls import path

from jobs.views.api import UpdateJobStatusApiView

# app_name = "bookkeeper"

urlpatterns = [
    path(
        "update-job-status",
        UpdateJobStatusApiView.as_view(),
        name="update-job-status",
    ),
]
