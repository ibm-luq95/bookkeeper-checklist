# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "client"

urlpatterns = [
    # path("api/", include("client.urls.api"), name="client-api-urls"),
    path("manager/", include("client.urls.manager"), name="client-manager-urls"),
    path("assistant/", include("client.urls.assistant"), name="client-assistant-urls"),
    # path(
    #     "bookkeeper/",
    #     include("client.urls.bookkeeper"),
    #     name="client-bookkeeper-urls",
    # ),
]
