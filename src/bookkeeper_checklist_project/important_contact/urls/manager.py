# -*- coding: utf-8 -*-#
from django.urls import path

from important_contact.views import (
    ManagerImportantContactUpdateView,
    ManagerImportantContactListView,
    ManagerImportantContactCreateView,
    ManagerImportantContactDeleteView,
)

app_name = "manager"

urlpatterns = [
    path("", ManagerImportantContactListView.as_view(), name="list"),
    path("create", ManagerImportantContactCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ManagerImportantContactUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ManagerImportantContactDeleteView.as_view(), name="delete"),
]
