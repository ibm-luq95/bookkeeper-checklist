# -*- coding: utf-8 -*-#
from django.urls import path, include
from jobs.views import (
    JobDeleteView,
    JobCreateView,
    JobDetailsView,
    JobListView,
    JobArchiveListView,
    JobUpdateView,
)

app_name = "jobs"

urlpatterns = [
    path("api/", include("jobs.urls.api"), name="jobs-api-urls"),
    path("templates/", include("jobs.urls.templates"), name="jobs-templates-urls"),
    # path("manager/", include("jobs.urls.manager"), name="jobs-manager-urls"),
    path("", JobListView.as_view(), name="list"),
    path("create", JobCreateView.as_view(), name="create"),
    path("archive", JobArchiveListView.as_view(), name="archive"),
    path("delete/<uuid:pk>", JobDeleteView.as_view(), name="delete"),
    path("update/<uuid:pk>", JobUpdateView.as_view(), name="update"),
    path("<uuid:pk>", JobDetailsView.as_view(), name="details"),
]
