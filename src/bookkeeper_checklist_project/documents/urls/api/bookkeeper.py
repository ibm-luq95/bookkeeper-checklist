# -*- coding: utf-8 -*-#
from django.urls import path

from documents.views.api import (
    CreateDocumentBookkeeperApiView,
    RetrieveDocumentBookkeeperApiView,
    DeleteDocumentBookkeeperApiView,
)

app_name = "bookkeeper"

urlpatterns = [
    path(
        "create",
        CreateDocumentBookkeeperApiView.as_view(),
        name="create",
    ),
    path("delete", DeleteDocumentBookkeeperApiView.as_view(), name="delete"),
    path("retrieve", RetrieveDocumentBookkeeperApiView.as_view(), name="retrieve"),
]
