# -*- coding: utf-8 -*-#
from django.urls import path
from bookkeeper.views import JobListView

app_name = "job"

urlpatterns = [
    path("", JobListView.as_view(), name="list"),
]
