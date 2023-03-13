# -*- coding: utf-8 -*-#
from django.urls import path, include

from documents.views.api import (
    CreateDocumentApiView,
    DeleteDocumentApiView,
    RetrieveDocumentApiView,
)

app_name = "api"

urlpatterns = [
    path(
        "create-document",
        CreateDocumentApiView.as_view(),
        name="create",
    ),
    path("delete", DeleteDocumentApiView.as_view(), name="delete"),
    path("retrieve", RetrieveDocumentApiView.as_view(), name="retrieve"),
    path(
        "templates/",
        include("documents.urls.api.templates"),
        name="documents-templates-api-urls",
    ),
]
