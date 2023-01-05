# -*- coding: utf-8 -*-#
from django.urls import path
from manager.views import (
    JobListView,
    JobCreateView,
    JobDetailsView,
    JobUpdateView,
    JobDeleteView,
)

app_name = "jobs"

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
    path("create", JobCreateView.as_view(), name="create"),
    path("details/<uuid:pk>", JobDetailsView.as_view(), name="details"),
    path("update/<uuid:pk>", JobUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>", JobDeleteView.as_view(), name="delete"),
]
