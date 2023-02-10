# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "accounts"

urlpatterns = [
    # path("api/", include("client.urls.api"), name="client-api-urls"),
    path(
        "manager/",
        include("client_account.urls.manager"),
        name="client-account-manager-urls",
    ),
    # path("assistant/", include("client.urls.assistant"), name="client-assistant-urls"),
    # path(
    #     "bookkeeper/",
    #     include("client.urls.bookkeeper"),
    #     name="client-bookkeeper-urls",
    # ),
]
