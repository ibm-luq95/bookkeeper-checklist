# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path(
        "manager/",
        include("jobs.urls.api.manager"),
        name="manager-jobs-api-urls",
    ),
    path(
        "bookkeeper/",
        include("jobs.urls.api.bookkeeper"),
        name="bookkeeper-jobs-api-urls",
    ),
]
