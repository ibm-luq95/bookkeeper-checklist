# -*- coding: utf-8 -*-#
from django.urls import path, include
from manager.views import (
    ClientAccountCreateView,
    ClientAccountListView,
    ClientAccountDetailView,
    ClientAccountUpdateView,
    ClientAccountDeleteView
)

app_name = "client_account"

urlpatterns = [
    path("", ClientAccountListView.as_view(), name="list"),
    path("create", ClientAccountCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ClientAccountUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ClientAccountDeleteView.as_view(), name="delete"),
    path("<uuid:pk>", ClientAccountDetailView.as_view(), name="details"),
]
