# -*- coding: utf-8 -*-#
from django.urls import path, include
from notes.views import NoteCreateView, NoteListView, NoteDeleteView, NotesUpdateView

app_name = "notes"

urlpatterns = [
    path("api/", include("notes.urls.api"), name="notes-api-urls"),
    path("", NoteListView.as_view(), name="list"),
    path("create", NoteCreateView.as_view(), name="create"),
    path("update/<uuid:pk>", NotesUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", NoteDeleteView.as_view(), name="delete"),
]
