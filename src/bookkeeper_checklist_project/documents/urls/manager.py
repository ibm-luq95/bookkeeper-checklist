# -*- coding: utf-8 -*-#
from django.urls import path

from documents.views import (
    ManagerUpdateDocumentView,
    ManagerCreateDocumentView,
    ManagerListDocumentView,
    ManagerDeleteDocumentView
)

app_name = "manager"

urlpatterns = [
    path("create/", ManagerCreateDocumentView.as_view(), name="create"),
    path("list/", ManagerListDocumentView.as_view(), name="list"),
    path("update/<uuid:pk>", ManagerUpdateDocumentView.as_view(), name="update"),
    path("delete/<uuid:pk>", ManagerDeleteDocumentView.as_view(), name="delete"),
]
