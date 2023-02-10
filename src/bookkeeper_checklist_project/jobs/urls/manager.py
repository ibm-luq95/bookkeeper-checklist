# -*- coding: utf-8 -*-#
from django.urls import path, include
from jobs.views import (
    ManagerJobListView,
    ManagerJobCreateView,
    ManagerJobArchiveListView,
    ManagerJobDetailsView,
    ManagerJobUpdateView,
    ManagerJobDeleteView,
)

app_name = "manager"

urlpatterns = [
    path("", ManagerJobListView.as_view(), name="list"),
    path("create", ManagerJobCreateView.as_view(), name="create"),
    path("archive", ManagerJobArchiveListView.as_view(), name="archive"),
    path("delete/<uuid:pk>", ManagerJobDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", ManagerJobUpdateView.as_view(), name="update"),
    path("<uuid:pk>", ManagerJobDetailsView.as_view(), name="details"),
]
