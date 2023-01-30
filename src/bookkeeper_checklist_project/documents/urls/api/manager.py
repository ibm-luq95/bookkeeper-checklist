# -*- coding: utf-8 -*-#
from django.urls import path

from documents.views.api import (
    CreateDocumentManagerApiView,
    DeleteDocumentManagerApiView,
    RetrieveDocumentManagerView,
)

app_name = "manager"

urlpatterns = [
    path(
        "create-document",
        CreateDocumentManagerApiView.as_view(),
        name="create",
    ),
    path("delete", DeleteDocumentManagerApiView.as_view(), name="delete"),
    path("retrieve", RetrieveDocumentManagerView.as_view(), name="retrieve"),
]
