# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "api"

urlpatterns = [
    path(
        "manager/",
        include("important_contact.urls.api.manager"),
        name="manager-important-contact-api-urls",
    ),
    path(
        "bookkeeper/",
        include("important_contact.urls.api.bookkeeper"),
        name="bookkeeper-important-contact-api-urls",
    ),
]
