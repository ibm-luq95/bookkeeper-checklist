# -*- coding: utf-8 -*-#
from django.urls import path

from jobs.views import (
    JobTemplatesListView,
    JobTemplateFactoryView,
    JobTemplateDetailsView,
    JobTemplateUpdateView,
)

app_name = "templates"

urlpatterns = [
    path("", JobTemplatesListView.as_view(), name="list"),
    path("factory", JobTemplateFactoryView.as_view(), name="create"),
    path("<uuid:pk>", JobTemplateDetailsView.as_view(), name="details"),
    path("update/<uuid:pk>", JobTemplateUpdateView.as_view(), name="update"),
]
