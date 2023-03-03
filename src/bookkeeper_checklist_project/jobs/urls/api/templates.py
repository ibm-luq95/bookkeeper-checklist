# -*- coding: utf-8 -*-#
from django.urls import path, include

from jobs.views.api import JobRetrieveTemplateApi

app_name = "templates"

urlpatterns = [
    path("retrieve/<uuid:pk>", JobRetrieveTemplateApi.as_view(), name="retrieve"),
]
