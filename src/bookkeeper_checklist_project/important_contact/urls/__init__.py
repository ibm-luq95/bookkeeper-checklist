# -*- coding: utf-8 -*-#
from django.urls import path, include
from important_contact.views import (
    ImportantContactUpdateView,
    ImportantContactDeleteView,
    ImportantContactCreateView,
    ImportantContactListView,
)

app_name = "important_contact"

urlpatterns = [
    path("api/", include("important_contact.urls.api"), name="important-contact-api-urls"),
    path("", ImportantContactListView.as_view(), name="list"),
    path("create", ImportantContactCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ImportantContactUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ImportantContactDeleteView.as_view(), name="delete"),
]
