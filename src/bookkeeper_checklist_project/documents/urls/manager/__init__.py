# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "manager"

urlpatterns = [
    path(
        "documents/",
        include("documents.urls.manager.documents"),
        name="manager-documents-urls",
    )
]
