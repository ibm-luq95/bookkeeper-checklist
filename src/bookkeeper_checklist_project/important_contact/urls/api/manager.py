# -*- coding: utf-8 -*-#
from django.urls import path

from important_contact.views.api import (
    UpdateImportantContactManagerApiView,
    RetrieveImportantContactManagerApiView,
)

app_name = "manager"

urlpatterns = [
    path("update", UpdateImportantContactManagerApiView.as_view(), name="update"),
    path("retrieve", RetrieveImportantContactManagerApiView.as_view(), name="retrieve"),
]
