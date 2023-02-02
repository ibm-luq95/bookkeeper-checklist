# -*- coding: utf-8 -*-#
from django.urls import path

from documents.views import UpdateDocumentAssistantView

app_name = "assistant"

urlpatterns = [
    # path("create/", CreateManagerDocumentView.as_view(), name="create"),
    # path("list/", ListManagerDocumentView.as_view(), name="list"),
    path("update/<uuid:pk>", UpdateDocumentAssistantView.as_view(), name="update"),
]
