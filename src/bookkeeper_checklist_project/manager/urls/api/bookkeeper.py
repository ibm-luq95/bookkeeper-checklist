# -*- coding: utf-8 -*-#
from django.urls import path
from manager.views.api import CreateJobToBookkeeper

urlpatterns = [
    path("create-job", CreateJobToBookkeeper.as_view(), name="create-job-bookkeeper")
]