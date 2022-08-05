# -*- coding: utf-8 -*-#
from django.urls import path, include

from users.views import LoginView

app_name = "users"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
]
