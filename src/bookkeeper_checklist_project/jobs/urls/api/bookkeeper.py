# -*- coding: utf-8 -*-#
from django.urls import path

from jobs.views.api import FetchJobBookkeeperApiView

app_name = "bookkeeper"

urlpatterns = [
    path(
        "fetch_job",
        FetchJobBookkeeperApiView.as_view(),
        name="fetch",
    ),
]
