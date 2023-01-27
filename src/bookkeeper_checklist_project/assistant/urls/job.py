# -*- coding: utf-8 -*-#
from django.urls import path
from assistant.views import (
    JobListView,
    JobCreateView
)

app_name = "job"

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
    path("create", JobCreateView.as_view(), name="create"),
]
