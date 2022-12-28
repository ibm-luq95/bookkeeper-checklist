# -*- coding: utf-8 -*-#
from django.urls import path

from important_contact.views.api import (
    RetrieveImportantContactBookkeeperApiView,
)

app_name = "bookkeeper"

urlpatterns = [
    path("retrieve", RetrieveImportantContactBookkeeperApiView.as_view(), name="retrieve"),
]
