# -*- coding: utf-8 -*-#
from django.urls import path, include
from client_account.views import (
    ManagerClientAccountUpdateView,
    ManagerClientAccountDetailsView,
    ManagerClientAccountDeleteView,
    ManagerClientAccountCreateView,
    ManagerClientAccountListView,
)

app_name = "manager"

urlpatterns = [
    path("", ManagerClientAccountListView.as_view(), name="list"),
    path("create", ManagerClientAccountCreateView.as_view(), name="create"),
    path("delete/<uuid:pk>", ManagerClientAccountDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", ManagerClientAccountUpdateView.as_view(), name="update"),
    path("<uuid:pk>", ManagerClientAccountDetailsView.as_view(), name="details"),
]
