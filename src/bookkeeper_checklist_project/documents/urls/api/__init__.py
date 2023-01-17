# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path(
        "manager/", include("documents.urls.api.manager"), name="manager-documents-api-urls"
    ),
    path(
        "bookkeeper/",
        include("documents.urls.api.bookkeeper"),
        name="bookkeeper-documents-api-urls",
    ),
]
