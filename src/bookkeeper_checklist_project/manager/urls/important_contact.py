# -*- coding: utf-8 -*-#
from django.urls import path

from manager.views.important_contact import (
    ImportantContactListView,
    ImportantContactCreateView,
    ImportantContactUpdateView,
    ImportantContactDeleteView
)

app_name = "important_contact"

urlpatterns = [
    path("", ImportantContactListView.as_view(), name="list"),
    path("create", ImportantContactCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", ImportantContactUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", ImportantContactDeleteView.as_view(), name="delete"),
]
