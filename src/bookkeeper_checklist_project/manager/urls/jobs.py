# -*- coding: utf-8 -*-#
from django.urls import path, include
from manager.views import JobListView, JobCreateView, JobDetailsView

app_name = "jobs"

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
    path("create", JobCreateView.as_view(), name="create"),
    path("details/<uuid:pk>", JobDetailsView.as_view(), name="details"),
]
