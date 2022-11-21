# -*- coding: utf-8 -*-#
from django.urls import path, include
from manager.views import (
    ClientAccountCreateView,
    ClientAccountListView,
    ClientAccountDetailView,
)

app_name = "client_account"

urlpatterns = [
    path("", ClientAccountListView.as_view(), name="list"),
    path("create", ClientAccountCreateView.as_view(), name="create"),
    path("<uuid:pk>", ClientAccountDetailView.as_view(), name="details"),
]
