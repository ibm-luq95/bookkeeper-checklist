# -*- coding: utf-8 -*-#
from django.urls import path

from documents.views import BookkeeperUpdateDocumentView

app_name = "bookkeeper"

urlpatterns = [
    # path("create/", CreateManagerDocumentView.as_view(), name="create"),
    # path("list/", ListManagerDocumentView.as_view(), name="list"),
    path("update/<uuid:pk>", BookkeeperUpdateDocumentView.as_view(), name="update"),
]
