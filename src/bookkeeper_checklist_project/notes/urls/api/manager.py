# -*- coding: utf-8 -*-#
from django.urls import path

from notes.views import (
    CreateNoteManagerApiView,
    RetrieveNoteManagerApiView,
    UpdateNoteManagerApiView,
    DeleteNoteManagerApiView,
)

app_name = "manager"

urlpatterns = [
    path(
        "create-note",
        CreateNoteManagerApiView.as_view(),
        name="create-note-manager",
    ),
    path(
        "retrieve-note",
        RetrieveNoteManagerApiView.as_view(),
        name="retrieve-note-manager",
    ),
    path(
        "update-note",
        UpdateNoteManagerApiView.as_view(),
        name="update-note",
    ),
    path("delete-note", DeleteNoteManagerApiView.as_view(), name="delete-note"),
]
