# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "important_contact"

urlpatterns = [
    path("api/", include("important_contact.urls.api"), name="important-contact-api-urls"),
    path(
        "manager/",
        include("important_contact.urls.manager"),
        name="important-contact-manager-urls",
    ),
]
