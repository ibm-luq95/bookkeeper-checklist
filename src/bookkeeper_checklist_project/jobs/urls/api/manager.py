# -*- coding: utf-8 -*-#
from django.urls import path

from jobs.views.api import CreateJobManagerApiView

app_name = "manager"

urlpatterns = [
    path(
        "create",
        CreateJobManagerApiView.as_view(),
        name="create",
    ),
]
