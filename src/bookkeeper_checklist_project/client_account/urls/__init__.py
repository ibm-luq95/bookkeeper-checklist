# -*- coding: utf-8 -*-#
from django.urls import path, include
from client_account.views import (
    ClientAccountUpdateView,
    ClientAccountDeleteView,
    ClientAccountCreateView,
    ClientAccountListView,
    ClientAccountDetailsView,
)

app_name = "accounts"

urlpatterns = [
    # path("api/", include("client.urls.api"), name="client-api-urls"),
    path("", ClientAccountListView.as_view(), name="list"),
    path("create", ClientAccountCreateView.as_view(), name="create"),
    path("delete/<uuid:pk>", ClientAccountDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", ClientAccountUpdateView.as_view(), name="update"),
    path("<uuid:pk>", ClientAccountDetailsView.as_view(), name="details"),
    # path(
    #     "manager/",
    #     include("client_account.urls.manager"),
    #     name="client-account-manager-urls",
    # ),
    # path("assistant/", include("client.urls.assistant"), name="client-assistant-urls"),
    # path(
    #     "bookkeeper/",
    #     include("client.urls.bookkeeper"),
    #     name="client-bookkeeper-urls",
    # ),
]
