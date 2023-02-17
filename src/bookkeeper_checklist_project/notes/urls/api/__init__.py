# -*- coding: utf-8 -*-#
from django.urls import path, include
from notes.views.api import (
    CreateNoteApiView,
    RetrieveNoteApiView,
    UpdateNoteApiView,
    DeleteNoteApiView,
)

app_name = "api"

urlpatterns = [
    path(
        "create-note",
        CreateNoteApiView.as_view(),
        name="create",
    ),
    path(
        "retrieve-note",
        RetrieveNoteApiView.as_view(),
        name="retrieve",
    ),
    path(
        "update-note",
        UpdateNoteApiView.as_view(),
        name="update",
    ),
    path("delete-note", DeleteNoteApiView.as_view(), name="delete"),
    # path("manager/", include("notes.urls.api.manager"), name="manager-notes-api-urls"),
    # path(
    #     "bookkeeper/",
    #     include("notes.urls.api.bookkeeper"),
    #     name="bookkeeper-notes-api-urls",
    # ),
]
