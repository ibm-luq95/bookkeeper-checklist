# -*- coding: utf-8 -*-#
from django.urls import path, include
from documents.views import (
    DetailsDocumentView,
    UpdateDocumentView,
    ListDocumentView,
    DeleteDocumentView,
    CreateDocumentView,
)

app_name = "documents"

urlpatterns = [
    path("api/", include("documents.urls.api"), name="documents-api-urls"),
    # path("manager/", include("documents.urls.manager"), name="documents-manager-urls"),
    # path("assistant/", include("documents.urls.assistant"), name="documents-assistant-urls"),
    # path(
    #     "bookkeeper/",
    #     include("documents.urls.bookkeeper"),
    #     name="documents-bookkeeper-urls",
    # ),
    path("create/", CreateDocumentView.as_view(), name="create"),
    path("list/", ListDocumentView.as_view(), name="list"),
    path("update/<uuid:pk>", UpdateDocumentView.as_view(), name="update"),
    path("delete/<uuid:pk>", DeleteDocumentView.as_view(), name="delete"),
]
