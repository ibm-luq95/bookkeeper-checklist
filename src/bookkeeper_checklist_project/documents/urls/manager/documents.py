# -*- coding: utf-8 -*-#
from django.urls import path

from documents.views import (
    CreateManagerDocumentView,
    ListManagerDocumentView,
    DetailsManagerDocumentView,
)

urlpatterns = [
    path("create/", CreateManagerDocumentView.as_view(), name="create"),
    path("list/", ListManagerDocumentView.as_view(), name="list"),
    path("<uuid:pk>", DetailsManagerDocumentView.as_view(), name="details"),
]
