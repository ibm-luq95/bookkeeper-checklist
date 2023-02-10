# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "jobs"

urlpatterns = [
    path("api/", include("jobs.urls.api"), name="jobs-api-urls"),
    path("manager/", include("jobs.urls.manager"), name="jobs-manager-urls"),
]
