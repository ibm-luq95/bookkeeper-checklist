# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "special_assignment"

urlpatterns = [
    path(
        "api/", include("special_assignment.urls.api"), name="special-assignment-api-urls"
    ),
]