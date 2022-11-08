# -*- coding: utf-8 -*-#
from django.urls import path
from manager.views.api import CreateJobToBookkeeper

app_name = "bookkeeper"

urlpatterns = [
    path("create-job", CreateJobToBookkeeper.as_view(), name="create-job-bookkeeper")
]
