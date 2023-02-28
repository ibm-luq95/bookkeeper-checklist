# -*- coding: utf-8 -*-#
from django.urls import path, include

app_name = "users"

urlpatterns = [
    path("auth/", include("users.urls.auth"), name="users-auth-urls"),
    path("", include("users.urls.manager"), name="users-manager-urls"),
]
