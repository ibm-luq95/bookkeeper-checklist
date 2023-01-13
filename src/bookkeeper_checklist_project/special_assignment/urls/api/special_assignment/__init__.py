# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "special_assignment"

urlpatterns = [
    path(
        "manager/",
        include("special_assignment.urls.api.special_assignment.manager"),
        name="manager-special-assignment-api-urls",
    ),
    path(
        "bookkeeper/",
        include("special_assignment.urls.api.special_assignment.bookkeeper"),
        name="bookkeeper-special-assignment-api-urls",
    ),
]
