# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "notes"

urlpatterns = [
    path("api/", include("notes.urls.api"), name="notes-api-urls"),
]
