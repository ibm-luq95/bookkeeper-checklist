# -*- coding: utf-8 -*-#
from django.urls import path

from notes.views import (
    CreateNoteBookkeeperApiView,
    RetrieveNoteBookkeeperApiView,
    UpdateNoteBookkeeperApiView,
    DeleteNoteBookkeeperApiView,
)

app_name = "bookkeeper"

urlpatterns = [
    path(
        "create",
        CreateNoteBookkeeperApiView.as_view(),
        name="create",
    ),
    path(
        "retrieve",
        RetrieveNoteBookkeeperApiView.as_view(),
        name="retrieve",
    ),
    path(
        "update",
        UpdateNoteBookkeeperApiView.as_view(),
        name="update",
    ),
    path("delete", DeleteNoteBookkeeperApiView.as_view(), name="delete"),
]
