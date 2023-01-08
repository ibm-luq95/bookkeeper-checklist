# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path(
        "discussion/",
        include("special_assignment.urls.api.discussion"),
        name="discussion-api-urls",
    ),
    path(
        "special_assignment/",
        include("special_assignment.urls.api.special_assignment"),
        name="manager-special-assignment-api-urls",
    ),
]
