# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "bookkeeper"

urlpatterns = [
    path(
        "documents/",
        include("documents.urls.bookkeeper.documents"),
        name="bookkeeper-documents-urls",
    )
]
