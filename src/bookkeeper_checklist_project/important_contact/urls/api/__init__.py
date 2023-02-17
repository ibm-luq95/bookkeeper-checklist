# -*- coding: utf-8 -*-#
from django.urls import path

from important_contact.views.api import (
    CreateImportantContactApiView,
    UpdateImportantContactApiView,
    RetrieveImportantContactApiView,
)

app_name = "api"

urlpatterns = [
    path("create", CreateImportantContactApiView.as_view(), name="create"),
    path("update", UpdateImportantContactApiView.as_view(), name="update"),
    path("retrieve", RetrieveImportantContactApiView.as_view(), name="retrieve"),
    # path(
    #     "manager/",
    #     include("important_contact.urls.api.manager"),
    #     name="manager-important-contact-api-urls",
    # ),
    # path(
    #     "bookkeeper/",
    #     include("important_contact.urls.api.bookkeeper"),
    #     name="bookkeeper-important-contact-api-urls",
    # ),
]
