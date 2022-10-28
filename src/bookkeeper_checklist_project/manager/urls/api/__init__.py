# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "bookkeeper_api"

urlpatterns = [
    path("bookkeeper/", include("manager.urls.api.bookkeeper"), name="mg-bookkeeper-api"),
]
