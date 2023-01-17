# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("manager/", include("notes.urls.api.manager"), name="manager-notes-api-urls"),
    path(
        "bookkeeper/",
        include("notes.urls.api.bookkeeper"),
        name="bookkeeper-notes-api-urls",
    ),
]
