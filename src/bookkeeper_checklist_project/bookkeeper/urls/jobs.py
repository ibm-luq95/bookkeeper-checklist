# -*- coding: utf-8 -*-#
from django.urls import path
from bookkeeper.views import JobListView, JobDetailView

app_name = "job"

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
    path("<uuid:pk>", JobDetailView.as_view(), name="details"),
]
