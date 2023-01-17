# -*- coding: utf-8 -*-#
from django.urls import path

from documents.views.api import (
    CreateDocumentManagerApiView,
    DeleteDocumentManagerApiView,
    RetrieveDocumentManagerView,
)

app_name = "manager_api"

urlpatterns = [
    path(
        "create-document",
        CreateDocumentManagerApiView.as_view(),
        name="create-document-manager",
    ),
    path("delete", DeleteDocumentManagerApiView.as_view(), name="delete-document"),
    path("retrieve", RetrieveDocumentManagerView.as_view(), name="retrieve"),
]
