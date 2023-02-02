# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "documents"

urlpatterns = [
    path("api/", include("documents.urls.api"), name="documents-api-urls"),
    path("manager/", include("documents.urls.manager"), name="documents-manager-urls"),
    path("assistant/", include("documents.urls.assistant"), name="documents-assistant-urls"),
    path(
        "bookkeeper/",
        include("documents.urls.bookkeeper"),
        name="documents-bookkeeper-urls",
    ),
]
